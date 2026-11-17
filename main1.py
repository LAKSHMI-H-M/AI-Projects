
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)

question = input("How can I assist you? ")

if question.strip():
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=question
    )
    print("\nGemini:", response.text)
else:
    print("Please enter a question.")
