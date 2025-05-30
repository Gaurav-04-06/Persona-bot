# 📘 Project Documentation – Persona Bot (Hitesh Choudhary AI)

This document outlines how the **Persona Bot** project was built, configured, and deployed using **Streamlit** and **Gemini Free API**.

---

## 🔧 Step-by-Step Setup

### 1. 💻 Project Structure

The project consists of the following core files:

```
├── main.py              # Streamlit app interface
├── chatbot.py           # Gemini-based chatbot logic
├── requirements.txt     # Python dependencies
├── .env                 # API key storage (locally)
├── assets/hitesh.jpeg   # Avatar image
└── README.md            # Project overview
```

---

### 2. 🧠 Language Model: Gemini (Google AI)

- Used `google-generativeai` Python package.
- Fetched API key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- Stored in `.env` for local and **Streamlit Secrets** (TOML) for deployment.

---

### 3. 🔐 Managing Secrets

#### Local:
Created a `.env` file with:

```
GEMINI_API_KEY=your_api_key_here
```

Used `python-dotenv` to load the key in Python.

#### Deployment (Streamlit Cloud):
Used TOML format in the secrets editor:

```toml
GEMINI_API_KEY = "AIzaSy...your_key..."
```

---

### 4. 🧠 Prompt Engineering

Since Gemini does not support a `system` role like OpenAI, we manually inserted the prompt at the beginning of the conversation to guide the chatbot’s behavior.

**Prompt Goal**: Simulate the tone, style, and teaching method of *Hitesh Choudhary*.

**Prompt Characteristics**:
- Used Hinglish (Hindi + English)
- Included motivational tone
- Provided teaching style with analogies, projects
- Always started replies with “Hanji”

**Prompt Injection Strategy**:
- On the first user message, the prompt was prepended like:

```python
prompt_with_context = SYSTEM_PROMPT.strip() + "\nUser: " + user_input
```

This ensures Gemini responds using the intended personality.

---

### 5. 🌍 Deployment on Streamlit Cloud

Steps followed:
1. Pushed project to GitHub.
2. Logged into [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Connected repo and selected `main.py` as the entry point.
4. Added API key via Secrets manager using valid TOML.
5. Deployed successfully — app now publicly accessible.

---

### ✅ Outcome

- Fully functional chatbot mimicking Hitesh Choudhary.
- Real-time conversation using Gemini 1.5 Flash API.
- Publicly hosted on Streamlit Cloud.
- Clean UI with avatar and chat experience.

---

## 🧾 Author

Built with ❤️ by [@Gaurav-04-06](https://github.com/Gaurav-04-06)
