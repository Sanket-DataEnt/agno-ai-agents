import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self,usecase, agent_team,user_message):
        self.usecase = usecase
        self.agent_team = agent_team
        self.user_message = user_message


    def display_result_on_ui(self):
        agent_team = self.agent_team
        user_message = self.user_message
        usecase = self.usecase

        # # User Input
        # user_input = st.text_input("Enter your question:")
        # print(user_input)

        # Display Response
        if user_message:
            with st.spinner("Thinking..."):
                response = agent_team.run(user_message)
                st.markdown(response.get_content_as_string())

    