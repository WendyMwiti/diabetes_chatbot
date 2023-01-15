from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Any, Text, Dict, List

class ActionDefaultFallback(Action):
    def init(self):
        # self.gpt3 = gpt3()
        super()._init_()

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(self, dispatcher, tracker, domain):
        query = tracker.latest_message['text']
        dispatcher.utter_message(text=gpt3(query))

        return []