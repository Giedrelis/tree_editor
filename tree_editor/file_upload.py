import streamlit as st
import base64
from io import BytesIO

# Function to convert file to be downloadable
def get_download_link(file, file_name, file_label='File'):
    buffer = BytesIO()
    buffer.write(file.getvalue())
    b64 = base64.b64encode(buffer.getvalue()).decode()
    href = f'<a href="data:file/octet-stream;base64,{b64}" download="{file_name}">{file_label}</a>'
    return href

st.title("File Uploader and Downloader")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Show details about the uploaded file
    st.write("Filename:", uploaded_file.name)
    st.write("Filetype:", uploaded_file.type)
    st.write("Filesize:", uploaded_file.size)

    # Download button
    st.markdown(get_download_link(uploaded_file, uploaded_file.name, 'Download File'), unsafe_allow_html=True)
