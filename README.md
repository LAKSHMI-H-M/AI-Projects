# Gemini Chatbot with Conversation Memory

## Project Overview
A simple interactive AI chatbot built using Python and the Gemini API. It maintains conversation context within a chat session, allowing users to ask follow-up questions.

## Technologies Used
- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv

## Features
- Interactive chatbot
- Continuous conversation using a while loop
- Conversation context using Gemini chat sessions
- Secure API key management using environment variables
- Exit functionality

## How to Run

1. Clone this repository.
2. Install the required packages:

   `pip install -r requirements.txt`

3. Create a `.env` file in the project folder:

   `GEMINI_API_KEY=your_api_key`

4. Run the application:

   `python main.py`

## Learning Outcomes
- Working with an LLM API
- Creating chat sessions
- Maintaining conversation context
- Managing environment variables securely