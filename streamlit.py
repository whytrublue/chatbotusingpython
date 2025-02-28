import streamlit as st
from gpt import run as gpt_run  # OpenAI GPT
from model import run as dialogpt_run  # DialoGPT
from streamlit_chat import message as st_message

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input section
if prompt := st.chat_input("Type your message here..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Choose the model (GPT-3.5-turbo or DialoGPT)
    model_type = st.selectbox("Choose Model", ["GPT-3.5", "DialoGPT"])
    
    if model_type == "GPT-3.5":
        reply = gpt_run(prompt)  # Uses OpenAI API
    else:
        reply = dialogpt_run(prompt)  # Uses DialoGPT model

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(reply)

    # Save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": reply})
