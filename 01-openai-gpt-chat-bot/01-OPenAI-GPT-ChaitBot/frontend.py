import streamlit as st
from backend import ask_gpt

st.title("ChaitBot with SKT")

question = st.text_input("Enter your question:")

if st.button("Ask"):
    if question:
        answer = ask_gpt(question)
        st.write(answer)
