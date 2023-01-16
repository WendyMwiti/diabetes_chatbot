from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Any, Text, Dict, List
import openai

class GPT3ResponseAction(Action):
    def __init__(self):
        super().__init__()
        openai.api_key =  ""
        self.model_engine = "text-davinci-003"
    def name(self):
        return "action_gpt3_response"
    
    async def run(self, dispatcher, tracker, domain):
        # Get the user's message
        message = tracker.latest_message['text']
        # Check if the message contains certain keywords or phrases related to diabetes
        diabetes_keywords = ["diabetes", "blood sugar", "meal plan", "diagnosis", "insulin", "glucose", "diet", "nutrition", "medicine", "mellitus", "HbA1c", "hypoglycemia", "hyperglycemia", "goodbye"]
        if any(keyword in message.lower() for keyword in diabetes_keywords):
            prompt = "question about diabetes: " + message
            response = self.gpt3(prompt)
            dispatcher.utter_message(text=response)
        else:
            dispatcher.utter_message(text="Sorry, I am not able to answer that question.")

    def gpt3(self, prompt):
        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop="end diabetes",
            temperature=0.5,
        )
        response = completion.choices[0].text
        return response