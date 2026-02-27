import easyocr
from PIL import Image
import os

# 1. Initialize the Reader
# 'kn' is for Kannada, 'en' is for English
print("Loading OCR models... (This takes a moment the first time)")
reader = easyocr.Reader(['kn', 'en']) 

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        return "Error: Image file not found!"
    
    print(f"Reading text from: {image_path}")
    
    # 2. Read the image
    # detail=0 gives us just the text without extra coordinates
    result = reader.readtext(image_path, detail=0)
    
    # 3. Join the list of lines into one big string
    full_text = " ".join(result)
    return full_text

# --- TEST IT ---
# Replace 'test_contract.jpg' with a photo of a document you have
test_image = "knowledge_base/sample_page.jpg" 
text = extract_text_from_image(test_image)

print("\n--- EXTRACTED TEXT ---")
print(text)