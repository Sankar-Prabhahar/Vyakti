import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCCYK1i7j_Wbb2ajVFr3zZRaCMMgZVTxtw"  # Your NEW key from new project

import google.genai as genai

client = genai.Client()

try:
    response = client.models.generate_content(
        model="models/gemini-1.5-flash",
        contents="Say hello"
    )
    print("✅ KEY WORKS!")
    print(response.text)
except Exception as e:
    print(f"❌ Still fails: {e}")
