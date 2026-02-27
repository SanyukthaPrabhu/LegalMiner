import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# 1. Load your 'Brain' (The Database from Phase 1)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_db = Chroma(persist_directory="./legal_db", embedding_function=embeddings)

# 2. Initialize the FREE Gemini Model
# REMOVED: version="v1" (This was causing the error)
# UPDATED: model="gemini-1.5-flash" (Stable production name)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    temperature=0
)

def audit_contract(messy_text):
    print("Gemini AI is auditing the contract... please wait.")
    
    # Task: Search your Legal Database for the actual law
    search_query = "Standard notice period and security deposit rules in India"
    relevant_laws = vector_db.similarity_search(search_query, k=2)
    law_context = "\n".join([doc.page_content for doc in relevant_laws])
    
    # Task: Final Audit Analysis
    prompt = f"""
    You are a legal expert. Below is a messy OCR text from a rental agreement and real Indian Law context.
    
    MESSY CONTRACT TEXT:
    {messy_text}
    
    LEGAL CONTEXT FROM DATABASE:
    {law_context}
    
    DIRECTIONS:
    1. Fix the OCR typos and identify the Notice Period and Rent/Deposit.
    2. Compare the contract terms to the Legal Context.
    3. Identify any RISKS and explain them simply. 
    4. If there is Kannada text, provide the explanation in both Kannada and English.
    """
    
    # We use .invoke() to get the final response
    response = llm.invoke(prompt)
    return response.content

# --- TEST IT ---
# Use the messy text you got from Phase 2
messy_ocr_output = "RHNTALAGRLLJILYT... notice period 1 month... rent 10000..." 
report = audit_contract(messy_ocr_output)

print("\n--- FINAL BILINGUAL AUDIT REPORT ---")
print(report)