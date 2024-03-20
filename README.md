# Kensei: Learn Japanese Characters with AI

### Overview
Kensei (Kanji Sensei) is a CrewAI-powered application designed to assist learners in mastering Japanese characters (Kanji) by generating exercises from real-world texts. By analyzing documents, URLs, or plain text, Kensei aims to provide a dynamic and context-rich learning experience tailored to each user's progression.

### Objective
The primary goal of Kensei is to use generative AI to enable users to read and understand Japanese characters by interacting with exercises derived from authentic texts. The exercises will focus on recognizing characters, understanding their meanings, translating them, and applying them in sentences.

### Features
- Character Tabulation and Translation: Extract Japanese characters from input sources (Docs, Text, URL), translate them into English, provide their reading in Hiragana (Yomigata), and cache this information for future reference. Characters will be rated on a scale of 1-5 based on their importance and frequency of use.

- Sentence Generation for Kanji Study: Create sentences incorporating new characters to aid in learning their usage in context.

- Exercise Creation for Review: Generate exercises consisting of sentences with a missing character and four candidate characters to choose from, enhancing recall and application skills.

- Implementation Strategy
The development of Kensei will involve creating a CrewAI application structured around specific agents and tasks designed to fulfill the application's objectives. Here's a high-level overview of the components involved:

### Agents
- Text Processor Agent: Responsible for fetching and processing input from various sources (documents, URLs, plain text) to extract Japanese text.

- Character Analyst Agent: Analyzes the extracted text to identify and tabulate Japanese characters, performs translations, and assigns importance ratings.

- Exercise Generator Agent: Utilizes the processed character data to create educational content, including contextual sentences and review exercises.

### Tasks
- Text Extraction Task: Extract text from the given input source, focusing on Japanese characters.

- Character Analysis Task: Translate the extracted characters, provide their readings, and rate their importance.

- Sentence Generation Task: Generate contextual sentences incorporating new characters for study purposes.

- Review Exercise Creation Task: Create exercises with fill-in-the-blank sentences and multiple-choice options for character selection.

### Tools and Integrations
- LLM Integration: Leverage a language model for translation, sentence generation, and exercise formulation.
- URL Processing Tool: Custom tool for extracting Japanese text from URLs.
- Database/Caching System: Store and manage character data, translations, and user progress.

### Getting Started
Instructions on setting up the environment, installing dependencies, and initializing the CrewAI project will be provided, ensuring users can easily set up Kensei for personal use.

