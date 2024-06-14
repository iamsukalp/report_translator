import streamlit as st
import pandas as pd
from tessaractApi import get_extracted_text
from prompt import get_prompt
from perplexityApi import get_result


st.set_page_config(layout="wide", page_title='Report Translator', page_icon=':speech_balloon:')



def download_file(translated_text,filename):
            st.download_button(
                label="Download file",
                data=translated_text,
                file_name= filename,
                mime="text/plain"
            )



def get_traslation(uplaoded_file):
    extracted_text = get_extracted_text(uplaoded_file)
    prompt = get_prompt(extracted_text)
    translated_text = get_result(prompt)
    filename = uplaoded_file.name
    filename = f"output/{filename.split('.')[0]}.txt"
    download_file(translated_text,filename)
     
    
def report_tab():
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf",key='translation')
    
    if st.button('Translate Report'):
        if uploaded_file is not None:
            get_traslation(uploaded_file)
        else:
            st.write('No file imported')
            


report_tab()
