from langchain.llms import OpenAI
from langchain.agents import load_tools,initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
import streamlit as st
from secret_key import Api_keys
import os
os.environ['OPENAI_API_KEY']=Api_keys
st.title("🤖Demo ChatBot")
st.sidebar.selectbox("History",("History of ChatGpt","History of user"))
llm=OpenAI(temperature=0,
           streaming=True
           )
tools=load_tools(['wikipedia','llm-math'],llm=llm)  # duckduckgo ,googlesearch

agent=initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

if prompt := st.chat_input("You: "):
    
    st.chat_message("user").write(prompt)
    with st.chat_message("assitant"):
        st.write("🧠thinking...")
        st_calback=StreamlitCallbackHandler(st.container())
        responce=agent.run(prompt,callbacks=[st_calback])
        st.write("🤖ai: ",responce)    