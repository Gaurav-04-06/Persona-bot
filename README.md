# 🤖 Persona Bot – Talk to Hitesh Choudhary (AI)

This project is an AI chatbot built with **Streamlit** and **Google Gemini Free API** that simulates the personality of **Hitesh Choudhary**, a renowned Indian educator and software engineer. The chatbot responds in Hitesh’s signature Hinglish style, using storytelling, analogies, and real-world project-based advice.

---

## 🚀 Features

- 🎙️ Emulates Hitesh Choudhary's tone and teaching style
- 🧠 Uses Gemini 1.5 Flash (Free API)
- 💬 Streamlit-based real-time chat interface
- 🔒 API key managed securely via `.env`
- 🖼️ Avatar-based chat display

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) – Frontend chat interface
- [Google Generative AI (Gemini)](https://ai.google.dev/) – Language model API
- [Python dotenv](https://pypi.org/project/python-dotenv/) – Manage secrets

---

## 📦 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/Gaurav-04-06/Persona-bot.git
cd Persona-bot
```

2. **Create a virtual environment (optional):**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add your Gemini API key:**

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

5. **Run the app:**

```bash
streamlit run main.py
```

---

## 📁 Project Structure

```bash
├── assets/
│   └── hitesh.jpeg           # Avatar for chat
├── chatbot.py                # Handles Gemini chat logic
├── main.py                   # Streamlit UI logic
├── requirements.txt
└── .env                      # Your Gemini API key
```

---


## 📌 Future Plans

- Add more personas (e.g., other educators or fictional characters)
- Voice integration 

---

## 🙏 Acknowledgements

- Inspired by [Hitesh Choudhary](https://www.youtube.com/c/HiteshChoudharyDotCom)
- Built with ❤️ by [@Gaurav-04-06](https://github.com/Gaurav-04-06)
