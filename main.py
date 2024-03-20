import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

class CustomCrew:
    def __init__(self, input_source):
        self.input_source = input_source

    def run(self):
        agents = CustomAgents()
        tasks = CustomTasks()

        text_processor_agent = agents.text_processor()
        character_analyst_agent = agents.character_analyst()
        exercise_generator_agent = agents.exercise_generator()

        text_extraction_task = tasks.text_extraction_task(text_processor_agent, self.input_source)
        character_analysis_task = tasks.character_analysis_task(character_analyst_agent)
        sentence_generation_task = tasks.sentence_generation_task(exercise_generator_agent)
        review_exercise_creation_task = tasks.review_exercise_creation_task(exercise_generator_agent)

        crew = Crew(
            agents=[text_processor_agent, character_analyst_agent, exercise_generator_agent],
            tasks=[text_extraction_task, character_analysis_task, sentence_generation_task, review_exercise_creation_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    print("## Welcome to Kanji Learning Crew AI")
    print("-------------------------------")
    input_source = input(dedent("""Enter the input source (document, text, or URL): """))

    custom_crew = CustomCrew(input_source)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your custom crew run result:")
    print("########################\n")
    print(result)