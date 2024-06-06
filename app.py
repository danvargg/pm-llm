import streamlit as st
from rag.chain import chain  # replace with the actual module name

st.title('PMBOK Questions')

question = st.text_input('Enter your question here:')
if question:
    answer = chain.invoke({"question": question})
    st.write(f'Answer: {answer}')
