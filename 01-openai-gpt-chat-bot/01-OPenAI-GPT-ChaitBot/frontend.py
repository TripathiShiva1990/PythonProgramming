import streamlit as st
from backend import ask_gpt

st.title("GPT App-By Shiva Tripathi")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        answer = ask_gpt(question)
        st.write(answer)
