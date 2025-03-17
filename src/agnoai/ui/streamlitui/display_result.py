import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self,agent_team,user_message):
        self.agent_team = agent_team
        self.user_message = user_message


    def display_result_on_ui(self):
        agent_team = self.agent_team
        user_message = self.user_message

        #  # Streamlit Interface
        # st.title("📈 Stock Analysis Expert")
        # # Description of the application
        # st.write("""
        # Welcome to the Stock Analysis Expert dashboard! This interactive app helps you analyze stock performance using key technical indicators. 
        # You can explore historical stock data, visualize trends, and make informed investment decisions.
        # """)

        # # User Input
        # user_input = st.text_input("Enter your question:")
        # print(user_input)

        # Display Response
        if user_message:
            with st.spinner("Thinking..."):
                response = agent_team.run(user_message)
                st.markdown(response.get_content_as_string())

    