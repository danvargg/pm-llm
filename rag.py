from operator import itemgetter  # TODO: make this section better
import os
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import DocArrayInMemorySearch

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

loader = PyPDFLoader('PMBOK7.pdf')
pages = loader.load_and_split()  # 11s to load the pmbok
# pages[100:105]

parser = StrOutputParser()

LLM = 'gpt-3.5-turbo'
# LLM = 'mixtral:8x7b'
# LLM = 'llama2'

if LLM.startswith('gpt-3'):
    model = ChatOpenAI(api_key=OPENAI_API_KEY, model=LLM)
    embeddings = OpenAIEmbeddings()
elif LLM.startswith('llama'):
    model = Ollama(model=LLM)
    embeddings = OllamaEmbeddings()

vector_store = DocArrayInMemorySearch.from_documents(
    pages, embedding=embeddings)  # 13s to index the pmbok, m s with llama2

template = """
Answer the question based on the context below. If you can't answer the question, reply "I don't know".

Context: {context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
# print(prompt.format(context="Here is some context", question="Here is a question"))


retriever = vector_store.as_retriever()

chain = (
    {
        "context": itemgetter("question")
        | retriever,
        "question": itemgetter("question")
    }
    | prompt
    | model
    | parser
)
# TODO: try .stream instead of .invoke
# chain.invoke({"question": "What is scope creep?"})  # 1s
# gpt: 'Scope creep is the uncontrolled expansion of product or project scope without adjustments to time, cost, and resources.'
# llama:
