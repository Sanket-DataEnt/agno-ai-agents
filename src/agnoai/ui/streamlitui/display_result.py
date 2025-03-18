import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

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

        # Display Response
        if user_message:
            with st.spinner("Good Things take time 🤔...."):
                response = final_agent.run(user_message)
                st.markdown(response.get_content_as_string())

    