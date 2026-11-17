#Example:keep questioning until user enters exit
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")

client = genai.Client(api_key=api_key)
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)

conversation = []

question = input("How can I assist you? ")
while question.strip().lower()!="exit":
    if question.strip():
        response = chat.send_message(question)
        print("\nGemini:", response.text)
    else:
        print("Please enter a question.")
    question = input("How can I assist you? ")
