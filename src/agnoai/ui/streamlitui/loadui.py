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
            
            # elif self.user_controls["selected_llm"] == 'Ollama':
            #     # Model selection
            #     model_options = self.config.get_ollama_model_options()
            #     self.user_controls["selected_ollama_model"] = st.selectbox("Select Model", model_options)

            #     # Download model with progress bar
            #     if st.button("Download Model"):
            #         self.download_model_with_progress_bar(self.user_controls["selected_ollama_model"])


            # Use case selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", usecase_options)

            if self.user_controls["selected_usecase"] == "Cooking Expert Agent":
                self.user_controls["EXA_API_KEY"] = st.session_state["EXA_API_KEY"] = st.text_input("EXA API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["EXA_API_KEY"]:
                    st.warning("⚠️ Please enter your EXA API key to proceed. Don't have? refer : https://dashboard.exa.ai/api-keys ")
            
            elif self.user_controls["selected_usecase"] == "Movie Recommender":
                self.user_controls["EXA_API_KEY"] = st.session_state["EXA_API_KEY"] = st.text_input("EXA API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["EXA_API_KEY"]:
                    st.warning("⚠️ Please enter your EXA API key to proceed. Don't have? refer : https://dashboard.exa.ai/api-keys ")
            
            elif self.user_controls["selected_usecase"] == "Books Recommender":
                self.user_controls["EXA_API_KEY"] = st.session_state["EXA_API_KEY"] = st.text_input("EXA API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["EXA_API_KEY"]:
                    st.warning("⚠️ Please enter your EXA API key to proceed. Don't have? refer : https://dashboard.exa.ai/api-keys ")

            elif self.user_controls["selected_usecase"] == "Travel Advisor":
                self.user_controls["EXA_API_KEY"] = st.session_state["EXA_API_KEY"] = st.text_input("EXA API Key",
                                                                                                      type="password")
                # Validate API key
                if not self.user_controls["EXA_API_KEY"]:
                    st.warning("⚠️ Please enter your EXA API key to proceed. Don't have? refer : https://dashboard.exa.ai/api-keys ")


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

        elif self.user_controls["selected_usecase"] == "YouTube Content Analyser":
            st.title("Youtube Video Analyser")
            st.write("""
            Welcome to the Youtube Video Analyst! that provides detailed video breakdowns, timestamps, and summaries. 
                     Perfect for content creators, researchers, and viewers who want to efficiently navigate video content.

            **Example Questions :**
            - Analyze this tech review: [video_url]
            - Get timestamps for this coding tutorial: [video_url]
            - Break down the key points of this lecture: [video_url]
            - Summarize the main topics in this documentary: [video_url]
            - Create a study guide from this educational video: [video_url]
                     
            **Note :** - OpenAI models works fine with YouTube Analyst.
                     
            """)

        elif self.user_controls["selected_usecase"] == "Research Agent":
            st.title("Research Agent")
            st.write("""
            Welcome to the News Research Agent! that combines web search capabilities with professional journalistic writing skills. 
                     The agent performs comprehensive research using multiple sources, fact-checks information, and delivers well-structured, 
                     TOI-style articles on any topic.
                     
            **Key capabilities:**

            - Advanced web search across multiple sources
            - Content extraction and analysis
            - Cross-reference verification
            - Professional journalistic writing
            - Balanced and objective reporting
            
            **Example prompts to try:**

            - Analyze the impact of AI on healthcare delivery and patient outcomes
            - Report on the latest breakthroughs in quantum computing
            - Investigate the global transition to renewable energy sources
            - Explore the evolution of cybersecurity threats and defenses
            - Research the development of autonomous vehicle technology        
            """)

        elif self.user_controls["selected_usecase"] == "Cooking Expert Agent":
            st.title("Your Personal Chef")
            st.write("""
            Welcome to the Cooking Expert Agent! that provides detailed, personalized recipes based on your ingredients, 
                     dietary preferences, and time constraints. The agent combines culinary knowledge, nutritional data, 
                     and cooking techniques to deliver comprehensive cooking instructions.

            **Example prompts to try:**
            
             - I have chicken, rice, and vegetables. What can I make in 30 minutes?
             - Create a vegetarian pasta recipe with mushrooms and spinach
             - Suggest healthy breakfast options with oats and fruits
             - What can I make with leftover turkey and potatoes?
             - Need a quick dessert recipe using chocolate and bananas
            """)

        elif self.user_controls["selected_usecase"] == "Movie Recommender":
            st.title("Your Movie Recommendation Assistant")
            st.write("""
            Welcome to the Movie Recommender! that provides comprehensive film suggestions based on your preferences.
                      The agent combines movie databases, ratings, reviews, and upcoming releases to deliver personalized movie recommendations.
            
            **Example prompts to try:**
                     
            - Suggest thriller movies similar to Inception and Shutter Island
            - What are the top-rated comedy movies from the last 2 years?
            - Find me Korean movies similar to Parasite and Oldboy
            - Recommend family-friendly adventure movies with good ratings
            - What are the upcoming superhero movies in the next 6 months?
            """)

        elif self.user_controls["selected_usecase"] == "Books Recommender":
            st.title("Your Books Recommendation Assistant")
            st.write("""
            Welcome to the Books Recommender! that provides comprehensive literary suggestions based on your preferences. 
                     The agent combines book databases, ratings, reviews, and upcoming releases to deliver personalized reading recommendations.

            **Example prompts to try:**

            - I loved ‘The Seven Husbands of Evelyn Hugo’ and ‘Daisy Jones & The Six’, what should I read next?
            - Recommend me some psychological thrillers like ‘Gone Girl’ and ‘The Silent Patient’
            - What are the best fantasy books released in the last 2 years?
            - I enjoy historical fiction with strong female leads, any suggestions?
            - Looking for science books that read like novels, similar to ‘The Immortal Life of Henrietta Lacks‘

            """)

        elif self.user_controls["selected_usecase"] == "Travel Advisor":
            st.title("Your Personal Travel Advisor")
            st.write("""
            Welcome to the Travel Asvisor! that  provides comprehensive itineraries and recommendations. 
                     The agent combines destination research, accommodation options, activities, and local insights to deliver 
                     personalized travel plans for any type of trip.

            **Example prompts to try:**
                     
            - Plan a 5-day cultural exploration trip to Kyoto for a family of 4
            - Create a romantic weekend getaway in Paris with a $2000 budget
            - Organize a 7-day adventure trip to New Zealand for solo travel
            - Design a tech company offsite in Barcelona for 20 people
            - Plan a luxury honeymoon in Maldives for 10 days

            """)
        

        return self.user_controls