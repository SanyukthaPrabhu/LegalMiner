import os
import requests

api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    print("API Key not found! Please set it in the terminal first.")
else:
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    response = requests.get(url)
    
    print("\n--- MODELS ALLOWED FOR YOUR API KEY ---")
    for model in response.json().get("models", []):
        name = model["name"].replace("models/", "")
        # We only want models that can generate text
        if "generateContent" in model.get("supportedGenerationMethods", []):
            print(name)
    print("---------------------------------------\n")