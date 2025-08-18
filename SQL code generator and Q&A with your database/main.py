from langchain_helper import main_function
import streamlit as st

st.title("Data_Analyzer: sql_code_generator and Q&A 🍩🍟🥗 ")

question= st.text_input("Question: ")
if question:
    chain = main_function()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)

