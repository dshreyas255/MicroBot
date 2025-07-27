import os
from dotenv import load_dotenv
import google.generativeai as genai

def configure_api():
    load_dotenv()  # Load from .env file
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing from the .env file.")
    genai.configure(api_key=api_key)

def main():
    configure_api()
    model = genai.GenerativeModel("gemini-2.5-pro")
    chat = model.start_chat()

    print("🤖 Gemini 2.5 Pro Chatbot (Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Bot: Goodbye!")
            break
        if not user_input:
            continue
        try:
            response = chat.send_message(user_input)
            print("Bot:", response.text)
        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()
