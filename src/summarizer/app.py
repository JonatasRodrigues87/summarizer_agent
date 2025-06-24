import asyncio
import streamlit as st
from agent import Agent

# Create a new event loop
loop = asyncio.new_event_loop()
# Set the event loop as the current event loop
asyncio.set_event_loop(loop)

st.set_page_config(layout="wide")
st.title("Welcome to the Summarizer Agent")
st.write("This app will help you to summerize text")

agent = Agent()

col1, col2 = st.columns(2)

with col1:
    request = st.text_area("Paste your text below:")
    button = st.button("send")

    box = st.container(height=300)
    with box:
        container = st.empty()
        container.text("Summarized text")
   
    if button:
        if request:          
           container.write("Processing...")  
           resumo = agent.sumarize_text(request)
           container.write(resumo)

   