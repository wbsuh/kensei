from crewai import Task
from textwrap import dedent

class CustomTasks:
    def text_extraction_task(self, agent, input_source):
        return Task(
            description=dedent(
                f"""
            As a Text Processor, your task is to extract Japanese text from the provided input source.
            
            Input Source: {input_source}
            
            Extract the Japanese text and pass it to the Character Analyst for further processing.
        """
            ),
            agent=agent,
            output_file='docs/extracted_text.txt',
            expected_output="Extracted Japanese characters/kanji text from the input source."  
        )

    def character_analysis_task(self, agent):
        return Task(
            description=dedent(
                f"""
            As a Character Analyst, your task is to analyze the extracted Japanese text, identify relevant characters, provide translations and Hiragana readings, and rate their importance on a scale of 1-5.
            
            The extracted Japanese text is located in the following file: docs/extracted_text.txt
            
            Provide the analysis results in the following format:
            Character | Translation | Hiragana Reading | Importance Rating
        """
            ),
            agent=agent,
            output_file='docs/character_analysis.csv',
            expected_output="Character analysis results in CSV format."  
        )
    
    def sentence_generation_task(self, agent):
        return Task(
            description=dedent(f"""\
            As an Exercise Generator, your task is to generate context-based sentences incorporating the analyzed characters.
            
            The character analysis results are located in the following file: docs/character_analysis.csv
            
            Generate sentences that provide meaningful context for learning the characters. Include a mix of characters with different importance ratings.
            """),
            agent=agent,
            output_file='docs/generated_sentences.txt',
            expected_output="Generated sentences incorporating the analyzed characters."  
        )
    
    def review_exercise_creation_task(self, agent):
        return Task(
            description=dedent(f"""\
            As an Exercise Generator, your task is to create review exercises based on the analyzed characters and generated sentences.
            
            The character analysis results are located in the following file: docs/character_analysis.csv
            The generated sentences are located in the following file: docs/generated_sentences.txt
            
            Create japanese sentence exercises with missing characters and provide four candidate characters for the user to choose from. Ensure a balanced mix of characters with different importance ratings.
            """),
            agent=agent,
            output_file='docs/review_exercises.txt',
            expected_output="Review exercises with missing characters and multiple-choice options."  
        )