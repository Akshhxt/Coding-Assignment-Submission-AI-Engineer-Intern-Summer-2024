import streamlit as st
import fitz  # PyMuPDF
import os
from transformers import pipeline

# Load pipelines with public models
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

# Function to convert PDF to text
def pdf_to_txt(pdf_path):
    pdf_document = fitz.open(pdf_path)
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Streamlit UI
st.title("Document Processing Chatbot")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])
if uploaded_file is not None:
    # Save the uploaded file
    pdf_path = os.path.join("uploaded_files", uploaded_file.name)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"Uploaded {uploaded_file.name}")
    
    # Convert PDF to text
    document_text = pdf_to_txt(pdf_path)
    st.subheader("Extracted Text")
    st.write(document_text)
    
    # Perform NER
    st.subheader("Named Entity Recognition (NER)")
    extracted_info = ner(document_text)
    st.json(extracted_info)
    
    # Classify document
    st.subheader("Document Classification")
    document_category = classifier(document_text)
    st.json(document_category)
    
    # Translate document
    st.subheader("Translate to French")
    translated_text = translator(document_text)[0]['translation_text']
    st.text_area("Translated Text", translated_text, height=300)
    
    # Feedback
    st.subheader("Feedback")
    feedback = st.text_area("Provide feedback on the extracted data")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")
