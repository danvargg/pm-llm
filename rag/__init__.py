import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


TEMPLATE = """
As an expert project and program manager, answer the question based on the context below.
If you can't answer the question, reply "I can't answer that with the information provided".

Context: {context}

Question: {question}
"""
