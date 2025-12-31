from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

# Load up the secrets (API keys) from the .env file
load_dotenv()


@CrewBase
class BlogCrew():
    """Blog writing crew class"""

    # These point to where our config files live
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['research_agent'],  # Grabs settings directly from agents.yaml
            tools=[SerperDevTool()],  # Give this agent Google search powers
            verbose=True
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer_agent'],  # Config handles the LLM connection automatically
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],  # Matches the 'research_task' entry in yaml
            agent=self.researcher()
        )

    @task
    def blog_task(self) -> Task:
        return Task(
            config=self.tasks_config['blog_task'],
            agent=self.writer()
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.writer()],
            tasks=[self.research_task(), self.blog_task()],
            process=Process.sequential,  # Run them one after another
            verbose=True
        )


if __name__ == "__main__":
    # Fire up the crew and ask it to write about EVs
    blog_crew = BlogCrew()
    result = blog_crew.crew().kickoff(inputs={"topic": "The future of electrical vehicles"})

    print("\n\n########################")
    print(result)