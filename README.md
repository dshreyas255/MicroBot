# 🤖 MicroBot

MicroBot is a lightweight, Gemini-powered chatbot application built using Python and Flask. It enables seamless interaction with Google's Gemini 2.5 Pro large language model through both a modern web interface and a command-line interface.

---

## 🌟 Features

- 🔮 Integrates with **Google Gemini 2.5 Pro** for conversational AI
- 🌐 Clean and responsive **web interface** using HTML, CSS, and JavaScript
- 🖥️ Minimal **command-line interface (CLI)** for quick usage
- 🔐 API key secured via `.env` file using `python-dotenv`
- ⚙️ Built with **Flask**, a powerful Python micro web framework
- ✅ Includes robust error handling and testable architecture

---

## 🗂️ Project Structure

```
MicroBot/
├── .env                # Stores your Gemini API key (not tracked)
├── chatbot.py          # CLI-based chatbot runner
├── server.py           # Flask server with RESTful endpoint for chat
├── templates/
│   └── index.html      # Frontend served via Flask
└── README.md           # This file
```

---

## 🚀 Getting Started

### 1️⃣ Prerequisites

- Python 3.8+
- Valid [Google Gemini API key](https://makersuite.google.com/app)

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/microbot.git
cd microbot
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### Sample `requirements.txt`

```
Flask==3.0.0
python-dotenv==1.0.1
google-generativeai==0.2.2
```

### 4️⃣ Set Up Environment

Create a `.env` file with your API key:

```env
GEMINI_API_KEY=your_actual_key_here
```

---

## 🧪 Usage

### 🔹 Command-Line Interface

```bash
python chatbot.py
```

### 🔹 Web Interface

```bash
python server.py
```

Then open your browser at:  
[http://localhost:5000](http://localhost:5000)

---

## ✅ Example Chat API

The `/chat` endpoint accepts a POST request with this JSON body:

```json
{
  "message": "Hello, how are you?"
}
```

It returns:

```json
{
  "response": "I'm doing great! How can I assist you today?"
}
```

---

## 🔍 Testing

To run unit tests:

```bash
pip install pytest
pytest tests/
```

Basic test ideas:
- `GET /` returns 200 OK
- `POST /chat` with no message returns 400
- `POST /chat` with valid input returns Gemini response

---

## 🧠 Design Highlights

- MVC-inspired separation: templates for view, `server.py` as controller, Gemini model as backend logic
- Uses **environment variables** to isolate credentials
- Built with extensibility and testability in mind

---

## 📌 Roadmap / Future Enhancements

- [ ] User authentication and chat session storage
- [ ] Real-time typing animation or streamed responses
- [ ] Docker container for portable deployment
- [ ] Custom memory or persona persistence

---

## 🤝 Contributing

Contributions are welcome! Please fork the repo, open an issue, or submit a pull request.

---

## 🙋‍♂️ Author

**Shreyas D**  
Feel free to reach out for suggestions or collaboration ideas.
