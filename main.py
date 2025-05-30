import streamlit as st
from chatbot import get_response
import os

st.set_page_config(page_title="Hitesh Choudhary AI", page_icon="🤖")
st.title("💬 Talk to Hitesh Choudhary (AI)")

# ✅ Load avatar once
hitesh_avatar = os.path.join("assets", "hitesh.jpeg")

# ✅ Initialize chat history if not done yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# ✅ User input box
user_input = st.chat_input("Ask your question...")

if user_input:
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        reply = get_response(user_input, st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})

# ✅ Display all messages in order
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant", avatar=hitesh_avatar):
            st.markdown(msg["content"])
