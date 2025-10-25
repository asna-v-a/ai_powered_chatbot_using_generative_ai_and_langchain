"""
Simple langchain streamlit app with groq
A beginner friendly versions focusing on core concepts
"""
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import os

## Page config
st.title("🚀 Simple Langchain Chatbot wth Groq")
st.markdown("Learn langchain basic with Groq's fast interface")

with st.sidebar:
    st.header("⚙️ Settings")
    api_key = st.text_input("Groq api key", type = "password", help="Get free api key from console.groq.com")
    model_name=st.selectbox(
        "Model",
        ["llama-3.1-8b-instant", "gemma2-9b-it"],
        index=0
    )
    if st.button("Clear Chat"):
        st.session_state.messages=[]
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages=[]

#### initilize LLM
@st.cache_resource
def get_chain(api_key, model_name):
    if not api_key:
        return None
    ##initilize chat model
    llm=ChatGroq(groq_api_key = api_key, model_name=model_name, streaming=True)
    prompt=ChatPromptTemplate.from_messages([
        "system", "You are a helpful assitanat powerd by groq . Answer Question Clearly and concisley."
        "user", "{question}"
    ])
    #####create a chain
    chain=prompt|llm|StrOutputParser()
    return chain

#### get chain##
chain = get_chain(api_key, model_name)
if not chain:
    st.warning("Please enter your groq api key in left sidebar to show output")
    st.markdown("(Get your free api key from http://console.groq.com)")
else:
    ### Display the chat message
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    ####chat input
    if question:=st.chat_input("Ask me anything"):
        ##Ask user message to session state
        with st.chat_message("user"):
            st.write(question)
    ## Generate response
    with st.chat_message("assitant"):
        message_placeholder=st.empty()
        full_response=""
        try:
            ## Stream response from groq
            for chunk in chain.stream({"question": question}):
                full_response += chunk
                message_placeholder.markdown(full_response + "")
            message_placeholder.markdown(full_response)
            ##Add to history
            st.session_state.messages.append({"role":"assitant", "content": full_response})
        except Exception as e:
            st.error(f"Error: {str(e)}")
### Examples
st.markdown("- - - - - - - ")
st.markdown("### Try these examples")
col1, col2 = st.columns(2)
with col1:
    st.markdown("🕵️... What is Langchain")
    st.markdown("📊... What is Machine Learning")
with col2:
    st.markdown("🧿... How do i learn programing")
    st.markdown("🤖... Write a story about AI")
###Fotter
st.markdown("- - - - - ")
st.markdown("Built with Langchain and Groq | Experience the Speed")