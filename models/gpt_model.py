import openai
import os
from dotenv import load_dotenv

load_dotenv()

class GPTModel:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
    
    def generate_description(self, prompt):
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
