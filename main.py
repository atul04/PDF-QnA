import os
import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
import multidocs_palm as mp
from htmlTemplates import css, bot_template, user_template, info_template

st.set_page_config(page_title="QnA PDFs", page_icon=":page_facing_up:")
st.write(css, unsafe_allow_html=True)

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    # print(response)

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
def main():
    base_dir = Path("main.py").resolve().parent
    base_dir = str(base_dir)
    load_dotenv()
    dotenv_path = base_dir+'/Keys/.env' 
    # print("Here -------------"+dotenv_path)
    load_dotenv(dotenv_path)  # take environment variables from .env (especially openai api key)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.title(':orange[QnA PDFs] :page_facing_up: :page_facing_up:')
    user_question = st.text_input("**Ask a question about your :blue[documents]:**")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader(":orange[Your documents]")
        uploaded_files = st.file_uploader(":blue[Upload your files here and click on 'Process Document']. Accepts :red[pdf files only.]", accept_multiple_files=True, type=['pdf'])
        if st.button('Process Document') and uploaded_files:
            with st.spinner("Processing your document(s)"):
                texts = mp.extract_docs(uploaded_files)
                text_chunks = mp.chunk_texts(texts)
                vectorstore = mp.get_vectorstore(text_chunks)
                st.session_state.conversation = mp.get_chain(vectorstore)
                st.success('Documents processed successfully!')

if __name__ == "__main__":
    main()
