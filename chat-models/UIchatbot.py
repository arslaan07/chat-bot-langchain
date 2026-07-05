import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

st.title("Mood based Chat Bot")

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

choice = st.radio(
    "Choose a mode:",
    options=[1, 2, 3],
    format_func=lambda x: {1: "Funny", 2: "Sad", 3: "Rude"}[x]
)

mode_map = {
    1: "You are funny agent",
    2: "You are a sad agent",
    3: "You are a rude agent",
}
mode = mode_map[choice]
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("You:")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    if prompt != "0":
        response = model.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))
        with st.chat_message("assistant"):
            st.write(response.content)
    else:
        st.stop()