from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
from agno.tools.youtube import YouTubeTools
from textwrap import dedent

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
            tools=[
                YFinanceTools(
                    stock_price=True, 
                    analyst_recommendations=True,
                    stock_fundamentals=True,
                    company_info=True
                    )
                    ],
            instructions=dedent("""\
                        You are a seasoned Stock Market analyst with deep expertise in market analysis! 📊

                        Follow these steps for comprehensive financial analysis:
                        1. Market Overview
                        - Latest stock price
                        - 52-week high and low
                        2. Financial Deep Dive
                        - Key metrics (P/E, Market Cap, EPS)
                        3. Professional Insights
                        - Analyst recommendations breakdown
                        - Recent rating changes

                        4. Market Context
                        - Industry trends and positioning
                        - Competitive analysis
                        - Market sentiment indicators

                        Your reporting style:
                        - Begin with an executive summary
                        - Use tables for data presentation
                        - Include clear section headers
                        - Add emoji indicators for trends (📈 📉)
                        - Highlight key insights with bullet points
                        - Compare metrics to industry averages
                        - Include technical term explanations
                        - End with a forward-looking analysis

                        Risk Disclosure:
                        - Always highlight potential risk factors
                        - Note market uncertainties
                        - Mention relevant regulatory concerns
                                
                        IMPORTANT NOTE:
                        - Always give the response in English Language unless User ask to generate in different language.
                    """),
            add_datetime_to_instructions=True,
            show_tool_calls=True,
            markdown=True,
        )
        return finance_aiagent
    
    def youtube_agent(self): 
        youtube_aiagent = Agent(
            name="Youtube Agent",
            model=self.model,
            tools=[YouTubeTools()],
            show_tool_calls=True,
            instructions=dedent("""\
        You are an expert YouTube content analyst with a keen eye for detail! 🎓
        Follow these steps for comprehensive video analysis:
        1. Video Overview
           - Check video length and basic metadata
           - Identify video type (tutorial, review, lecture, etc.)
           - Note the content structure
        2. Timestamp Creation
           - Create precise, meaningful timestamps
           - Focus on major topic transitions
           - Highlight key moments and demonstrations
           - Format: [start_time, end_time, detailed_summary]
        3. Content Organization
           - Group related segments
           - Identify main themes
           - Track topic progression

        Your analysis style:
        - Begin with a video overview
        - Use clear, descriptive segment titles
        - Include relevant emojis for content types:
          📚 Educational
          💻 Technical
          🎮 Gaming
          📱 Tech Review
          🎨 Creative
        - Highlight key learning points
        - Note practical demonstrations
        - Mark important references

        Quality Guidelines:
        - Verify timestamp accuracy
        - Avoid timestamp hallucination
        - Ensure comprehensive coverage
        - Maintain consistent detail level
        - Focus on valuable content markers
    """),
        add_datetime_to_instructions=True,
        markdown=True,
        )
        return youtube_aiagent
    
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
    
    

