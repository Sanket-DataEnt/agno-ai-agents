from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

class Agents:
    def __init__(self, user_controls_input, model):
        self.user_controls_input=user_controls_input
        self.model = model
    
    def web_agent(self):
        web_aiagent = Agent(
            name="Web Agent",
            role="Search the web for information",
            # model=self.user_controls_input["selected_llm"],
            model=self.model,
            tools=[DuckDuckGoTools()],
            instructions="Always include sources",
            show_tool_calls=True,
            markdown=True,
        )
        return web_aiagent

    def finance_agent(self):
        finance_aiagent = Agent(
            name="Finance Agent",
            role="Get Financial Data",
            # model=self.user_controls_input["selected_llm"],
            model=self.model,
            tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,stock_fundamentals=True,company_info=True)],
            instructions="Use tables to display data",
            show_tool_calls=True,
            markdown=True,
        )
        return finance_aiagent
    
    def agent_team(self):
        agent_aiteam = Agent(
        team = [self.web_agent(), self.finance_agent()],
        # model = self.user_controls_input["selected_llm"],
        model=self.model,
        instructions=["Always include sources", "Use tables to display data"],
        show_tool_calls=True,
        markdown=True,
        )
        return agent_aiteam
    
    

