import streamlit as st 
import os 

uploaded_files = st.sidebar.file_uploader("Choose a file",type=["PDF","XML","TXT"])
submitted = st.sidebar.button("Submit")
if submitted:
    directory = r"C:\Users\karthikeyan\OneDrive\Desktop\Notepad"
    path = os.path.join(directory,uploaded_files.name)
    with open(path,"rb") as f:
        data = f.read()
        data = data.decode("utf-8")
        st.write(data)
    
    