import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Initialize the agent
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
    instructions="Use tables to display data",
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


# Streamlit Interface
st.title("📈 Stock Analysis Expert")
# Description of the application
st.write("""
Welcome to the Stock Analysis Expert dashboard! This interactive app helps you analyze stock performance using key technical indicators. 
You can explore historical stock data, visualize trends, and make informed investment decisions.
""")

# User Input
user_input = st.text_input("Enter your question:")
print(user_input)

# Display Response
if user_input:
    with st.spinner("Thinking..."):
        response = agent_team.run(user_input)
        st.markdown(response.get_content_as_string())
