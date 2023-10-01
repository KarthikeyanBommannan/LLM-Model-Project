import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
from  langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import os 
# from htmlTemplates import css, bot_template, user_template
api_key = "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"
os.environ["OPENAI_API_KEY"] = api_key

def get_pdf_text(document):
    text = ""
    for pdf in document:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vetorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    #embeddings = HuggingFaceInstructEmbeddings(model_name = "hkunlp/instructor-xl"     )
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True,max_history=5) 
    conversation_chain = ConversationalRetrievalChain.from_llm(
                                                                llm=llm,
                                                                retriever=vectorstore.as_retriever(),
                                                                memory=memory
                                                             )
    return conversation_chain


def handle_userinput(user_question):
     response = st.session_state.conversation({"question":user_question})
     st.write(response["answer"])






def main():
    load_dotenv()
    st.set_page_config(layout="wide",page_title="Chat with PDF",page_icon=":books:")
    # st.write(css,unsafe_allow_html=True)
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    st.header("Chat with PDF")
    user_question = st.text_input("Ask your Question about your documents")
    if user_question:
        handle_userinput(user_question)
    
    # st.write(user_template.replace("{{MSG}}","Hello"),unsafe_allow_html=True)
    # st.write(bot_template.replace("{{MSG}}","Hello"),unsafe_allow_html=True)
    
    with st.sidebar:
        document = st.file_uploader(":green[Upload a PDF file]",type = ["PDF"],accept_multiple_files=True)
        if st.button("Submit"):
            with st.spinner("Loading..."):
                # get the PDF Text 
                raw_text = get_pdf_text(document)
                
                # get the text from the PDF
                text_chunks = get_text_chunks(raw_text)
        
                # create vector store 
                vectorstore = get_vetorstore(text_chunks)  
                
                st.session_state.conversation = get_conversation_chain(vectorstore)






if __name__ == "__main__":
    main()