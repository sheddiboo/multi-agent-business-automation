import os
from datetime import datetime
from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, DirectoryReadTool, FileWriterTool, FileReadTool
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables (API Keys for Cerebras, Groq, and Serper)
load_dotenv()

# --- LLM CONFIGURATIONS ---

# Cerebras: Optimized for high-reasoning tasks and long-form strategy.
# Using llama-3.3-70b for deep analysis and research-heavy roles.
cerebras_llm = LLM(
    model="cerebras/llama-3.3-70b",
    api_key=os.getenv("CEREBRAS_API_KEY"),
    temperature=0.7
)

# Groq: Optimized for high-speed content generation.
# Used here for creative writing and rapid social media drafting.
groq_llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7,
)


# --- DATA SCHEMAS ---

class Content(BaseModel):
    """Structured output for marketing materials to ensure consistency across agents."""
    content_type: str = Field(..., description="Type of content (e.g., Blog, Reel Script, Social Post)")
    topic: str = Field(..., description="The main subject of the content")
    target_audience: str = Field(..., description="The specific segment being addressed")
    tags: List[str] = Field(..., description="SEO and metadata tags")
    content: str = Field(..., description="The full body text in Markdown format")


@CrewBase
class TheMarketingCrew():
    """
    Orchestrates a multi-agent pipeline for automated marketing strategy and content creation.
    Inspired by the Codebasics framework, adapted for a Cerebras/Groq hybrid architecture.
    """

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # --- AGENT DEFINITIONS ---

    @agent
    def head_of_marketing(self) -> Agent:
        """Responsible for market research and high-level strategy orchestration."""
        return Agent(
            config=self.agents_config['head_of_marketing'],
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
                DirectoryReadTool(directory='resources/drafts'),
                FileWriterTool(),
                FileReadTool()
            ],
            llm=cerebras_llm,
            allow_delegation=False,
            verbose=True
        )

    @agent
    def content_creator_social_media(self) -> Agent:
        """Focused on rapid generation of short-form social content and video scripts."""
        return Agent(
            config=self.agents_config['content_creator_social_media'],
            llm=groq_llm,
            allow_delegation=False,
            max_rpm=2,  # Throttled to respect production tier rate limits
            verbose=True
        )

    @agent
    def content_writer_blogs(self) -> Agent:
        """Specialized in long-form, authoritative blog writing and technical documentation."""
        return Agent(
            config=self.agents_config['content_writer_blogs'],
            llm=cerebras_llm,
            allow_delegation=False,
            verbose=True
        )

    @agent
    def seo_specialist(self) -> Agent:
        """Ensures all generated content is optimized for search engines and keywords."""
        return Agent(
            config=self.agents_config['seo_specialist'],
            llm=cerebras_llm,
            allow_delegation=False,
            verbose=True
        )

    # --- TASK DEFINITIONS ---

    @task
    def market_research(self) -> Task:
        """Executes initial market analysis and competitive landscape review."""
        return Task(config=self.tasks_config['market_research'], agent=self.head_of_marketing())

    @task
    def prepare_marketing_strategy(self) -> Task:
        """Synthesizes research into a comprehensive Markdown strategy document."""
        return Task(config=self.tasks_config['prepare_marketing_strategy'], agent=self.head_of_marketing(),
                    output_file="resources/drafts/marketing_strategy.md")

    @task
    def create_content_calendar(self) -> Task:
        """Plans out the distribution schedule for the generated marketing assets."""
        return Task(config=self.tasks_config['create_content_calendar'], agent=self.head_of_marketing(),
                    output_file="resources/drafts/content_calendar.md")

    @task
    def prepare_post_drafts(self) -> Task:
        """Generates structured social media post drafts using Groq for speed."""
        return Task(config=self.tasks_config['prepare_post_drafts'], agent=self.content_creator_social_media(),
                    output_json=Content)

    @task
    def prepare_scripts_for_reels(self) -> Task:
        """Creates scripts for short-form video content."""
        return Task(config=self.tasks_config['prepare_scripts_for_reels'], agent=self.content_creator_social_media(),
                    output_json=Content)

    @task
    def content_research_for_blogs(self) -> Task:
        """Gathers specific data points and references for long-form blog posts."""
        return Task(config=self.tasks_config['content_research_for_blogs'], agent=self.content_writer_blogs())

    @task
    def draft_blogs(self) -> Task:
        """Drafts full blog articles in structured JSON format."""
        return Task(config=self.tasks_config['draft_blogs'], agent=self.content_writer_blogs(), output_json=Content)

    @task
    def seo_optimization(self) -> Task:
        """Final audit of all content to maximize visibility and reach."""
        return Task(config=self.tasks_config['seo_optimization'], agent=self.seo_specialist(), output_json=Content)

    @crew
    def marketingcrew(self) -> Crew:
        """Assembles the agents and tasks into a sequential workflow."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Tasks are completed in order
            verbose=True,
            planning=False,
            max_rpm=5  # Safeguard for API rate limiting across the entire crew
        )


if __name__ == "__main__":
    # Define product and campaign parameters
    inputs = {
        "product_name": "AI Powered Excel Automation Tool",
        "target_audience": "Small and Medium Enterprises (SMEs)",
        "product_description": "A tool that automates repetitive tasks in Excel using AI, saving time and reducing errors.",
        "budget": "NGN. 500,000",
        "current_date": datetime.now().strftime("%Y-%m-%d"),
    }

    # Initialize and kickoff the marketing pipeline
    marketing_crew = TheMarketingCrew()
    result = marketing_crew.marketingcrew().kickoff(inputs=inputs)

    # Output the final marketing materials
    print("\n--- Marketing Pipeline Execution Complete ---")
    print(result)