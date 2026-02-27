import streamlit as st
import os
from ocr_engine import extract_text_from_image
from auditor import audit_contract

st.set_page_config(page_title="LexiCheck: AI Legal Auditor", layout="wide")

st.title("⚖️ LexiCheck: Bilingual AI Legal Auditor")
st.subheader("VTU AIML Project - Sanyuktha Prabhu")

# Sidebar for instructions
with st.sidebar:
    st.header("How to use")
    st.write("1. Upload a photo of a Rental Agreement.")
    st.write("2. AI will read the text (OCR).")
    st.write("3. AI will audit risks based on Indian Law.")

# File Uploader
uploaded_file = st.file_uploader("Upload Contract Image (JPG/PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Save the file temporarily
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    col1, col2 = st.columns(2)

    with col1:
        st.image(uploaded_file, caption="Uploaded Document", use_column_width=True)
        
    with col2:
        with st.spinner("Extracting text (OCR)..."):
            extracted_text = extract_text_from_image("temp_image.jpg")
            st.success("Text Extracted!")
            st.text_area("OCR Output", extracted_text, height=200)

    if st.button("🚀 Run AI Legal Audit"):
        with st.spinner("Analyzing against Legal Database..."):
            report = audit_contract(extracted_text)
            st.markdown("### 📜 Final Legal Audit Report")
            st.info(report)