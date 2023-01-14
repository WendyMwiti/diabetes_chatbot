#This files contains your custom actions which can be used to run
#custom Python code.

#See this guide on how to implement these action:
#https://rasa.com/docs/rasa/custom-actions


#This is a simple example for a custom action which utters "Hello World!"

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from typing import Any, Text, Dict, List

ALLOWED_DIABETES_TYPES = ["type 1 diabetes", "type 2 diabetes", "gestational diabetes"]

class AskForSufferAction(Action):
    def name(self) -> Text:
        return "action_ask_suffer"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text="Do you suffer from diabetes?",
            buttons=[
                {"title": "yes", "payload": "/affirm"},
                {"title": "no", "payload": "/deny"},
            ],
        )
        return []

    

class AskForTypeAction(Action):
    def name(self) -> Text:
        return "action_ask_type"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        if tracker.get_slot("suffer"):
            dispatcher.utter_message(
                text=f"What kind of diabetes do you suffer from?",
                buttons=[{"title": p, "payload": p} for p in ALLOWED_DIABETES_TYPES],
            )
        else:
            dispatcher.utter_message(
                text=f"What do you want to know about diabetes?",
            )
        return []

class ValidateSufferFromDiabetesForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_suffer_from_diabetes_form"
        
    def validate_suffer(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        if tracker.get_intent_of_latest_message() == "affirm":
            dispatcher.utter_message(
                text="Not to worry. I'm here to support you with diabetes resources. It can be managed!"
            )
            return {"suffer": True}
        if tracker.get_intent_of_latest_message() == "deny":
            dispatcher.utter_message(
                text="A healthy lifestyle can help keep it this way. What else would like to know about diabetes?."
            )
            return {"suffer": False}
        dispatcher.utter_message(text="I didn't get that.")
        return {"suffer": None}


def validate_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        

        if slot_value not in ALLOWED_DIABETES_TYPES:
            dispatcher.utter_message(
                text=f"I don't recognize that pizza. We serve {'/'.join(ALLOWED_DIABETES_TYPES)}."
            )
            return {"type": None}
        if not slot_value:
            dispatcher.utter_message(
                text=f"I don't recognize that. We serve {'/'.join(ALLOWED_PIZZA_TYPES)}."
            )
            return {"type": None}
        dispatcher.utter_message(text=f"OK! Not to worry! {slot_value} is a condition that can be managed. I'm here to support with resources on the same")
        return {"type": slot_value}

