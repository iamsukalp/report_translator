import pdfplumber
import pytesseract
from PIL import Image
import io
import streamlit as st

# pytesseract.pytesseract.tesseract_cmd = r"https://github.com/learntripathi/report_translator/tree/main/Tesseract-OCR/tesseract.exe"

# @st.cache_resource
# def find_tesseract_binary() -> str:
#     return shutil.which("tesseract")

# pytesseract.pytesseract.tesseract_cmd = find_tesseract_binary()

# if not pytesseract.pytesseract.tesseract_cmd:
#     st.error("Tesseract binary not found in PATH. Please install Tesseract.")

# Function to convert PDF page to image and then to bytes
def pdf_page_to_image_bytes(page):
    # Convert pdfplumber page to image
    image = page.to_image(resolution=300)  # This gives you a PIL image directly
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)
    return img_byte_array.read()

# Extract text from each page of the PDF
def get_extracted_text(pdf_path):
    text_results = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            # Convert the PDF page to bytes
            img_bytes = pdf_page_to_image_bytes(page)

            # Perform OCR on the image using pytesseract
            text = pytesseract.image_to_string(Image.open(io.BytesIO(img_bytes)), lang='fra')  # 'fra' for French
            text_results.append(text)

    # Combine text results from all pages
    full_text = '\n\n'.join(text_results)
    
    return full_text


