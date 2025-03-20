import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json
import asyncio
from streamlit_lottie import st_lottie
import requests
import time

def render_animation():
    # https://lottiefiles.com/free-animations/websites
    # animation_url = "https://assets1.lottiefiles.com/packages/lf20_vykpwt8b.json"
    animation_url = "https://lottie.host/b625e5d3-e696-4bc2-a836-7fdd61efa527/daK5Y4g6cq.json" # Aeroplane Earth
    # animation_url = "https://lottie.host/0e344c09-4687-4a08-9e97-16dba5d1e479/f1jX44fp9f.json" # Thinking
    animation_response = requests.get(animation_url)
    if animation_response.status_code == 200:
        animation_json = animation_response.json()
        return st_lottie(animation_json, height=200, width=300)
    else:
        print("Error in the URL")


class DisplayResultStreamlit:
    def __init__(self,usecase, final_agent, user_message):
        self.usecase = usecase
        self.final_agent = final_agent
        self.user_message = user_message


    def display_result_on_ui(self):
        final_agent = self.final_agent
        user_message = self.user_message
        usecase = self.usecase

        # # User Input
        # user_input = st.text_input("Enter your question:")
        # print(user_input)

        # # Display Response
        if user_message:
            with st.spinner("Thinking 🤔...."):
                render_animation()
                response = final_agent.run(user_message)
                st.markdown(response.get_content_as_string())

    