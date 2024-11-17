from ultility import model
import streamlit as st
from streamlit_chat import message as st_message


# text = st.chat_input('please type your question here')
# if text:
#     reply = model.run(text)
#     st_message(reply)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("please type your question here?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    reply = model.run(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(reply)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": reply})


