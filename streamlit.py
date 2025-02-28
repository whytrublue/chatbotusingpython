import streamlit as st
from gpt import run as gpt_run  # OpenAI GPT-3.5
from model import run as dialogpt_run  # DialoGPT local model
from streamlit_chat import message as st_message

st.title("🤖 AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message here..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    # Select AI model
    model_type = st.radio("Choose Model", ["GPT-3.5", "DialoGPT"], index=0)

    # Get response
    reply = gpt_run(prompt) if model_type == "GPT-3.5" else dialogpt_run(prompt)

    with st.chat_message("assistant"):
        st.markdown(reply)

    # Store messages
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": reply})
