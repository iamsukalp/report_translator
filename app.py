import streamlit as st
import pandas as pd
from tessaractApi import get_extracted_text
from prompt import get_prompt
from perplexityApi import get_result


st.set_page_config(layout="wide", page_title='Report Translator', page_icon=':speech_balloon:')



def download_file(file_path, file_name):
        with open(file_path, "rb") as file:
            btn = st.download_button(
                label="Download file",
                data=file,
                file_name=file_name,
                mime="text"
            )


def save_text_file(uplaoded_file,translated_text):
    with open(f"{uplaoded_file.name}.txt", "w") as file:
        file.write(translated_text)
    


def get_traslation(uplaoded_file):
    extracted_text = get_extracted_text(uplaoded_file)
    prompt = get_prompt(extracted_text)
    translated_text = get_result(prompt)
    
    save_text_file(uplaoded_file,translated_text)
    filename = uplaoded_file.name
    filename = f"{filename.split('.')[0]}.txt"
    download_file(filename,filename)
     
    
def report_tab():
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf",key='translation')
    
    if st.button('Translate Report'):
        if uploaded_file is not None:
            get_traslation(uploaded_file)
        else:
            st.write('No file imported')
            


report_tab()
