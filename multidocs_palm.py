import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
import openai
from tenacity import retry, wait_random_exponential, stop_after_attempt

def load_model():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("Please set the OPENAI_API_KEY environment variable.")
        return None
    gpt_llm = OpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo", temperature=0.1)
    return gpt_llm

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def completion_with_retry(**kwargs):
    return openai.Completion.create(**kwargs)

def extract_docs(uploaded_files):
    texts = ""
    for pdf in uploaded_files:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            texts += page.extract_text()
    return texts

def chunk_texts(texts):
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', ' ', ''],
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_text(texts)
    return text_chunks

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_chain(vectorstore):
    gpt_llm = load_model()
    if not gpt_llm:
        return None
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=gpt_llm,
        retriever=vectorstore.as_retriever(),
        memory=memory)
    return conversation_chain
