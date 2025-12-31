import os
from datetime import datetime
from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
    SerperDevTool,
    ScrapeWebsiteTool,
    DirectoryReadTool,
    FileWriterTool,
    FileReadTool
)
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load Environment Variables
load_dotenv()

# Define the LLM
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.7,
)


# Define Structured Output Model
class Content(BaseModel):
    content_type: str = Field(..., description="The type of content (e.g., blog, social post, video script)")
    topic: str = Field(..., description="The main topic of the content")
    target_audience: str = Field(..., description="The target audience for the content")
    tags: List[str] = Field(..., description="Tags to be used for the content")
    content: str = Field(..., description="The content itself formatted in Markdown")


@CrewBase
class TheMarketingCrew():
    """
    The marketing crew is responsible for creating and executing marketing strategies,
    content creation, and managing marketing campaigns.
    """
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- AGENTS ---

    @agent
    def head_of_marketing(self) -> Agent:
        return Agent(
            config=self.agents_config['head_of_marketing'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool(directory='resources/drafts'),
                FileWriterTool(),
                FileReadTool()
            ],
            verbose=True,
            llm=llm,
            allow_delegation=True,
            max_rpm=30
        )

    @agent
    def content_creator_social_media(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator_social_media'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool(directory='resources/drafts'),
                FileWriterTool(),
                FileReadTool()
            ],
            verbose=True,
            llm=llm,
            allow_delegation=False,
            max_iter=30,
            max_rpm=30
        )

    @agent
    def content_writer_blogs(self) -> Agent:
        return Agent(
            config=self.agents_config['content_writer_blogs'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool(directory='resources/drafts/blogs'),
                FileWriterTool(),
                FileReadTool()
            ],
            verbose=True,
            llm=llm,
            allow_delegation=False,
            max_iter=10,
            max_rpm=30
        )

    @agent
    def seo_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['seo_specialist'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool(directory='resources/drafts'),
                FileWriterTool(),
                FileReadTool()
            ],
            verbose=True,
            llm=llm,
            allow_delegation=False,
            max_iter=5,
            max_rpm=30
        )

    # --- TASKS ---

    @task
    def market_research(self) -> Task:
        return Task(
            config=self.tasks_config['market_research'],
            agent=self.head_of_marketing()
        )

    @task
    def prepare_marketing_strategy(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_marketing_strategy'],
            agent=self.head_of_marketing(),
            output_file="resources/drafts/marketing_strategy.md"
        )

    @task
    def create_content_calendar(self) -> Task:
        return Task(
            config=self.tasks_config['create_content_calendar'],
            # Assigned to Head of Marketing (Strategy Lead)
            agent=self.head_of_marketing(),
            output_file="resources/drafts/content_calendar.md"
        )

    @task
    def prepare_post_drafts(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_post_drafts'],
            agent=self.content_creator_social_media(),
            output_json=Content  # Force structured JSON output
        )

    @task
    def prepare_scripts_for_reels(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_scripts_for_reels'],
            agent=self.content_creator_social_media(),
            output_json=Content
        )

    @task
    def content_research_for_blogs(self) -> Task:
        return Task(
            config=self.tasks_config['content_research_for_blogs'],
            agent=self.content_writer_blogs()
        )

    @task
    def draft_blogs(self) -> Task:
        return Task(
            config=self.tasks_config['draft_blogs'],
            agent=self.content_writer_blogs(),
            output_json=Content
        )

    @task
    def seo_optimization(self) -> Task:
        return Task(
            config=self.tasks_config['seo_optimization'],
            agent=self.seo_specialist(),
            output_json=Content
        )

    # --- CREW ---

    @crew
    def marketingcrew(self) -> Crew:
        """Creates the Marketing crew"""
        return Crew(
            agents=self.agents,  # Auto-collects all @agent decorated methods
            tasks=self.tasks,  # Auto-collects all @task decorated methods
            process=Process.sequential,
            verbose=True,
            planning=True,
            planning_llm=llm,
            max_rpm=30
        )


if __name__ == "__main__":
    # Define Inputs
    inputs = {
        "product_name": "AI Powered Excel Automation Tool",
        "target_audience": "Small and Medium Enterprises (SMEs)",
        "product_description": "A tool that automates repetitive tasks in Excel using AI, saving time and reducing errors.",
        "budget": "Rs. 50,000",
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }

    # Initialize and Kickoff
    print("### Starting Marketing Crew ###")
    marketing_crew = TheMarketingCrew()
    result = marketing_crew.marketingcrew().kickoff(inputs=inputs)

    print("\n\n########################")
    print("## Crew Execution Complete ##")
    print("########################\n")
    print(result)