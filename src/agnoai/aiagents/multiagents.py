# from agents import Agents
from agno.agent import Agent
from agno.team.team import Team


class MultiAgents:
    def __init__(self, Agents, model):
        self.Agents = Agents
        self.model = model

    def agent_team(self):
        agent_aiteam = Agent(
        team = [self.Agents.web_agent(), self.Agents.finance_agent()],
        model=self.model,
        instructions=["Always include sources", "Use tables to display data"],
        # show_tool_calls=True,
        markdown=True,
        )
        return agent_aiteam
    
    def discussion_team(self):
        discussion_aiteam = Team(
        name="Discussion Team",
        mode="collaborate",
        model=self.model,
        members=[
        self.Agents.reddit_researcher(),
        self.Agents.hackernews_researcher(),
        self.Agents.academic_paper_researcher(),
        self.Agents.twitter_researcher(),
        ],
        instructions=[
        "You are a discussion master.",
        "You have to stop the discussion when you think the team has reached a consensus.",
        ],
        success_criteria="The team has reached a consensus.",
        enable_agentic_context=True,
        # share_member_interactions=True,
        # show_tool_calls=True,
        markdown=True,
        debug_mode=True,
        show_members_responses=True,
        )
        return discussion_aiteam
    

