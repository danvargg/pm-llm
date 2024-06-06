from operator import itemgetter  # TODO: make this section better

from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.prompts import ChatPromptTemplate
from langchain_community.vectorstores import DocArrayInMemorySearch

from rag.models import model, embeddings
from rag import TEMPLATE

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

loader = PyPDFLoader('PMBOK7.pdf')
pages = loader.load_and_split()  # 11s to load the pmbok
# pages[100:105]

parser = StrOutputParser()

vector_store = DocArrayInMemorySearch.from_documents(
    pages, embedding=embeddings)  # 13s to index the pmbok, m s with llama2

prompt = ChatPromptTemplate.from_template(TEMPLATE)
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

# chain = (
#     {
#         "context": lambda x: x["question"]
#         | retriever,
#         "question": lambda x: x["question"]
#     }
#     | prompt
#     | model
#     | parser
# )

# TODO: implement chatgpt suggestion on chromadb

# TODO: try .stream instead of .invoke
# chain.invoke({"question": "What is scope creep?"})  # 1s
# gpt: 'Scope creep is the uncontrolled expansion of product or project scope without adjustments to time, cost, and resources.'
# llama:
# TODO: use llama model without ollama desktop
