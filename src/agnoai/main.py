import streamlit as st
import json
from src.agnoai.ui.streamlitui.loadui import LoadStreamlitUI
from src.agnoai.LLMs.groqllm import GroqLLM
from src.agnoai.LLMs.openaillm import OpenAILLM
# from src.agnoai.LLMs.ollamallm import OllamaLLM
from src.agnoai.aiagents.agents import Agents
from src.agnoai.ui.streamlitui.display_result import DisplayResultStreamlit

# Main Function 
def load_agno_agenticai_app():

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            if user_input['selected_llm']=='Groq':
                obj_llm_config = GroqLLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()

                if not model:
                    st.error("Error: LLM model could not be initialized.")
                    return
            elif user_input['selected_llm']=='OpenAI':
                obj_llm_config = OpenAILLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()

                if not model:
                    st.error("Error: LLM model could not be initialized.")
                    return
                
            # elif user_input['selected_llm']=='Ollama':
            #     obj_llm_config = OllamaLLM(user_controls_input=user_input)
            #     model = obj_llm_config.get_llm_model()

            #     if not model:
            #         st.error("Error: LLM model could not be initialized.")
            #         return
            
            usecase = user_input.get('selected_usecase')
            if not usecase:
                    st.error("Error: No use case selected.")
                    return
            
            ### Agents
            agents = Agents(user_input, model)
            if usecase=="Stock Analyser":
                 final_agent = agents.agent_team()
            elif usecase=="YouTube Content Analyser":
                 final_agent = agents.youtube_agent()
            elif usecase=="Research Agent":
                 final_agent = agents.research_agent()
            elif usecase=="Cooking Expert Agent":
                 final_agent = agents.recipe_agent()
            elif usecase=="Movie Recommender":
                 final_agent=agents.movieRecommender_agent()
            elif usecase=="Books Recommender":
                 final_agent=agents.book_recommendation_agent()
            elif usecase=="Travel Advisor":
                 final_agent=agents.travel_agent()
            

            DisplayResultStreamlit(usecase, final_agent, user_message).display_result_on_ui()
            
        
        except Exception as e:
                 raise ValueError(f"Error Occurred with Exception : {e}")  