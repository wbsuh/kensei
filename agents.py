from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool
)

docs_tool = DirectoryReadTool(directory='./docs')
file_tool = FileReadTool()

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-0125-preview", temperature=0.1)

    def text_processor(self):
        return Agent(
            role="Text Processor",
            backstory=dedent(f"""As a Text Processor, your role is to extract Japanese text from various input sources, such as documents, text, or URLs. You have extensive experience in text processing and are proficient in handling different file formats and encodings."""),
            goal=dedent(f"""Extract Japanese text from the provided input source and pass it to the Character Analyst for further processing."""),
            tools=[file_tool, docs_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
    
    def character_analyst(self):
        return Agent(
            role="Character Analyst",
            backstory=dedent(f"""As a Character Analyst, you are an expert in Japanese language and linguistics. Your role is to analyze Japanese text, identify relevant characters, provide translations, and rate their importance for learning."""),
            goal=dedent(f"""Analyze the extracted Japanese text, identify characters, provide translations and Hiragana readings, and rate their importance on a scale of 1-5."""),
            tools=[file_tool, docs_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4, 
        )

    def exercise_generator(self):
            return Agent(
                role="Exercise Generator",
                backstory=dedent(f"""As an Exercise Generator, you specialize in creating effective learning materials for Japanese language learners. Your expertise lies in generating context-based sentences and review exercises that facilitate language acquisition."""),
                goal=dedent(f"""Generate context-based sentences incorporating the analyzed characters and create review exercises with missing characters and multiple-choice options."""),
                tools=[file_tool, docs_tool],
                allow_delegation=False,
                verbose=True,
                llm=self.OpenAIGPT4,
            )