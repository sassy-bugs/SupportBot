# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
import json
import random
import datetime
from typing import Dict, Text, Any, List, Optional
import logging
from rasa_sdk.interfaces import Action
from rasa_sdk.events import (
    SlotSet,
    EventType,
    ActionExecuted,
    SessionStarted,
    Restarted,
    FollowupAction,
    UserUtteranceReverted,
    ActionExecutionRejected
)
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict


logger = logging.getLogger(__name__)

class ActionInternship(Action):

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "internship_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Executes the action"""
        slots = ["kind_of_internship", "placeofwork", "domain_of_interest", "work_mode"]

        for slot in slots:
            if slot not in tracker.slots:
                dispatcher.utter_template("utter_ask_{}".format(slot), tracker)
                return [SlotSet(slot, None)]
        


        kind_of_internship = tracker.get_slot("kind_of_internship")
        placeofwork = tracker.get_slot("placeofwork")
        domain_of_interest = tracker.get_slot("domain_of_interest")
        work_mode = tracker.get_slot("work_mode")

        # Search for the internship in DB
        # If found, return the internship
        # If not found, return None
        # If multiple found, return all of them in a list
        


        dispatcher.utter_message("We have received the following information:")
        dispatcher.utter_message("Kind of internship: {}".format(kind_of_internship))
        dispatcher.utter_message("Place of work: {}".format(placeofwork))
        dispatcher.utter_message("Domain of interest: {}".format(domain_of_interest))
        dispatcher.utter_message("Work mode: {}".format(work_mode))
        return [SlotSet(slot, None) for slot in slots]

class ActionJob(Action):

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "job_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Executes the action"""
        slots = ["placeofwork", "domain_of_interest", "work_mode"]

        for slot in slots:
            if slot not in tracker.slots:
                dispatcher.utter_template("utter_ask_{}".format(slot), tracker)
                return [SlotSet(slot, None)]
        
        placeofwork = tracker.get_slot("placeofwork")
        domain_of_interest = tracker.get_slot("domain_of_interest")
        work_mode = tracker.get_slot("work_mode")
        dispatcher.utter_message("We have received the following information:")
        dispatcher.utter_message("Place of work: {}".format(placeofwork))
        dispatcher.utter_message("Domain of interest: {}".format(domain_of_interest))
        dispatcher.utter_message("Work mode: {}".format(work_mode))

        #Search for job in DB
        #If found, return the job
        #If not found, return None
        #If multiple found, return all of them in a list


        return [SlotSet(slot, None) for slot in slots]

class ActionOpportunity(Action):

    def name(self) -> Text:
        """Unique identifier for the action."""
        return "opportunity_form"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Executes the action"""
        slots = ["Type", "level", "placeofwork", "domain_of_interest", "work_mode"]

        for slot in slots:
            if slot not in tracker.slots:
                dispatcher.utter_template("utter_ask_{}".format(slot), tracker)
                return [SlotSet(slot, None)]
        


        Type = tracker.get_slot("Type")
        level = tracker.get_slot("level")
        placeofwork = tracker.get_slot("placeofwork")
        domain_of_interest = tracker.get_slot("domain_of_interest")
        work_mode = tracker.get_slot("work_mode")

        # Search for the opportunity in DB
        # If found, return the opportunity
        # If not found, return None
        # If multiple found, return all of them in a list


        dispatcher.utter_message("We have received the following information:")
        dispatcher.utter_message("Type: {}".format(Type))
        dispatcher.utter_message("level: {}".format(level))
        dispatcher.utter_message("place of work: {}".format(placeofwork))
        dispatcher.utter_message("domain of interest: {}".format(domain_of_interest))
        dispatcher.utter_message("work mode: {}".format(work_mode))
        return [SlotSet(slot, None) for slot in slots]