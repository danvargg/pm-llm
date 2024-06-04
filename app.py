import streamlit as st
import rag  # replace with the actual module name

st.title('PMBOK Questions')

question = st.text_input('Enter your question here:')
if question:
    answer = rag.chain.invoke({"question": question})
    st.write(f'Answer: {answer}')
