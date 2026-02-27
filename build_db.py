import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# 1. LOAD: Tell Python where your PDF is
# Make sure you have a PDF inside a folder named 'knowledge_base'
file_path = "knowledge_base/contract_act.pdf" 

if not os.path.exists(file_path):
    print(f"ERROR: I can't find the file at {file_path}. Check the folder name!")
else:
    loader = PyPDFLoader(file_path)
    data = loader.load()

    # 2. SPLIT: Break the long law into small pieces (chunks)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(data)

    # 3. EMBED: Turn words into numbers using a free AI model
    print("Turning text into vectors... this might take a minute.")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. STORE: Save these numbers into a local database folder
    vector_db = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory="./legal_db"
    )

    print("✅ Finished! Your 'legal_db' folder has been created.")