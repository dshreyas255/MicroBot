# server script
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up model
model = genai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat()

# Set up Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_with_bot():
    data = request.get_json()
    user_input = data.get("message", "")
    if not user_input:
        return jsonify({"response": "No message received."}), 400
    try:
        response = chat.send_message(user_input)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
