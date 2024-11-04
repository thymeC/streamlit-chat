import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage


# From here down is all the StreamLit UI.
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Hey, I'm your Chat GPT")

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") or st.sidebar.text_input('Enter your OpenAI API key:', type='password')

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful assistant.")
    ]


def load_answer(question):
    st.session_state.messages.append(HumanMessage(content=question))
    assistant_answer = chat(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content


def get_text():
    input_text = st.text_input("Question: ", key=input)
    return input_text


chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=api_key)

user_input = get_text()
submit = st.button('Generate')

if submit:
    response = load_answer(user_input)
    st.subheader("Answer:")
    st.write(response, key=1)
