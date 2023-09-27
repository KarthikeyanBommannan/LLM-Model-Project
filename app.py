import streamlit as st 

uploaded_files = st.file_uploader("Choose a file",type=["PDF","XML"])
submitted = st.button("Submit")
if submitted:
    print(uploaded_files)
    
    
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

