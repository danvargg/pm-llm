from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama

from rag import OPENAI_API_KEY

LLM = 'gpt-3.5-turbo'
# LLM = 'mixtral:8x7b'
# LLM = 'llama2'

if LLM.startswith('gpt-3'):
    model = ChatOpenAI(api_key=OPENAI_API_KEY, model=LLM)
    embeddings = OpenAIEmbeddings()
elif LLM.startswith('llama'):
    model = Ollama(model=LLM)
    embeddings = OllamaEmbeddings()
