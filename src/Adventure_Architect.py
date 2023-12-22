import streamlit as st

from Utility.OpenAIConnection import generate_text_raw
from Utility.ChatHelper import chat_prompt, chat_first_message

st.set_page_config(layout="centered")


with st.sidebar:
    "[All Icons created by Freepik - Flaticon](https://www.flaticon.com/authors/freepik)"

st.title("Adventure Architect")
st.caption("Your trusted companion that helps you make your adventures faster and more fun!")

icons = {"assistant": "assets/spellbook.png", "user": "assets/elf.png"}

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": chat_first_message},
                                    {"role": "system", "content": chat_prompt}]

for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"], avatar=icons[msg["role"]]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar=icons["user"]).write(prompt)
    with st.spinner('Seeking guidance from ancient spirits...'):
        msg = generate_text_raw(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant", avatar=icons["assistant"]).write(msg)
