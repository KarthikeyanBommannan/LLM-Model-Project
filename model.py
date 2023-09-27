from langchain.chat_models import ChatAnthropic
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.schema import AIMessage, HumanMessage, SystemMessages
import os
from dotenv import load_dotenv 
import PyPDF2
import streamlit as st

load_dotenv()

class Explorer:
    def __init__(self):
        """
        Initializes the class by setting the `system_prompt` and `user_prompt` 
        attributes and creating the chat and chain objects.

        Parameters:
        None

        Returns:
        None
        """
        self.system_prompt = self.get_system_prompt()
        self.user_prompt = HumanMessagePromptTemplate.from_template("{question}")
        full_prompt_template = ChatPromptTemplate.from_messages(
            [self.system_prompt, self.user_prompt]
        )
        
        self.chat = ChatAnthropic()
        self.chain = LLMChain(llm=self.chat,prompt =full_prompt_template)
        
    def get_system_prompt(self) -> str:
        """
        Get the system prompt from the uploaded file.

        Returns:
            str: The system prompt from the uploaded file.
        """
        uploaded_files = st.sidebar.file_uploader("Choose a file",type=["PDF","XML","TXT"])
        submitted = st.sidebar.button("Submit")
        if submitted:
            directory = r"C:\Users\karthikeyan\OneDrive\Desktop\Notepad"
            path = os.path.join(directory,uploaded_files.name)
            with open(path,"rb") as f:
                data = f.read()
                data = data.decode("utf-8")
                system_prompt = data
        return system_prompt
    
    def run_chain(self,language,question):
        return self.chain.run(language=language,question=question)
    
    
def retrieve_pdf_text(pdf_file):
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text