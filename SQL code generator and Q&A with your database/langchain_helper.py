import cryptography
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate
from few_shots import  few_shots
# load the llm
import os
from dotenv import load_dotenv
load_dotenv()

# load llm and setup
def main_function():
    # Load LLM
    llm = GoogleGenerativeAI(
        model="models/gemini-2.0-flash",
        google_api_key=os.environ["GOOGLE_API_KEY"],
        temperature=0.1
    )

    # Connect MySQL database
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_name = "langchain"

    db = SQLDatabase.from_uri(
        f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
        sample_rows_in_table_info=3
    )

    # HuggingFace embeddings
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    # Vectorize few_shots and store in FAISS
    to_vectorize = [" ".join(example.values()) for example in few_shots]
    vectorstore = FAISS.from_texts(to_vectorize, embeddings, metadatas=few_shots)

    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2
    )

    # Prompt for LLM
    Mysql_prompt = """
You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run,
then look at the results of the query and return the answer to the input question.

Unless the user specifies in the question a specific number of examples to obtain,
query for at most {top_k} results using the LIMIT clause as per MySQL.

Never query for all columns from a table. You must query only the columns that are needed to answer the question.
Wrap each column name in backticks (`) to denote them as delimited identifiers.

Use only the column names you can see in the tables below. Do not query for columns that do not exist.
Use CURDATE() if the question involves "today".

IMPORTANT:
- Output runnable SQL and its answer  without any markdown formatting, code blocks, or preamble.
- Do NOT use ```sql or the word 'sql' before the query.
- Return only the raw SQL query.
- Follow the SQLQuery format in few_shots.

Format:
Question: Question here
SQLQuery: Query to run with no preamble
SQLResult: Result of the SQLQuery
Answer: Final answer here
"""

    # Clean SQL helper
    def clean_sql(sql_text: str) -> str:
        return (
            sql_text.replace("```sql", "")
            .replace("```", "")
            .replace("SQLQuery:", "")
            .strip()
        )

    from langchain_experimental.sql.base import SQLDatabaseChain

    class CleanSQLDatabaseChain(SQLDatabaseChain):
        def _call(self, inputs, run_manager=None):
            result = super()._call(inputs, run_manager=run_manager)
            if "SQLQuery" in result:
                result["SQLQuery"] = clean_sql(result["SQLQuery"])
            return result

    # Few-shot example prompt
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {SQLResult}"
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=Mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"]
    )

    # Create chain
    chain = CleanSQLDatabaseChain.from_llm(
        llm, db, verbose=True, prompt=few_shot_prompt
    )

    return chain

# if __name__ == "__main__":
#     chain = main_function()
#     print(chain.invoke("Retrieve the top 10 highest-revenue orders?"))
