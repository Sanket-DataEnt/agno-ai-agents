import streamlit as st
import os
from datetime import date

# from langchain_core.messages import AIMessage,HumanMessage
from src.agnoai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config =  Config() 
        self.user_controls = {}

    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    }

    def load_streamlit_ui(self):
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False

        with st.sidebar:
            # Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)

            if self.user_controls["selected_llm"] == 'Groq':
                # Model selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                # API key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")

            elif self.user_controls["selected_llm"] == 'OpenAI':
                # Model selection
                model_options = self.config.get_openai_model_options()
                self.user_controls["selected_openai_model"] = st.selectbox("Select Model", model_options)
                # API key input
                self.user_controls["OPENAI_API_KEY"] = st.session_state["OPENAI_API_KEY"] = st.text_input("API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["OPENAI_API_KEY"]:
                    st.warning("⚠️ Please enter your OpenAI API key to proceed. Don't have? refer : https://platform.openai.com/api-keys ")

            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()

        if self.user_controls["selected_usecase"] == "Stock Analyser":
            # Streamlit Interface
            st.title("📈 Stock Analysis Expert")
            # Description of the application
            st.write("""
            Welcome to the Stock Analysis Expert dashboard! This interactive app helps you analyze stock performance using key technical indicators. 
            You can explore historical stock data, visualize trends, and make informed investment decisions.
            Please mention the Stock ticker/symbol for the analysis.
                     
            **Example Questions:**
            - Analyze the market outlook and financial performance of AI semiconductor company NVDA And Tesla And sugggest whether I have to buy or not?
            - What's the latest news and financial performance of Apple (AAPL)?
            - Give me a detailed analysis of Tesla's (TSLA) current market position
            - How are Microsoft's (MSFT) financials looking? Include analyst recommendations
            - Analyze NVIDIA's (NVDA) stock performance and future outlook
            - What's the market saying about Amazon's (AMZN) latest quarter?
            """)
        

        return self.user_controls