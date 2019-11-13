from textblob import TextBlob
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

class ActionCheckLinguality(Action):

    def name(self) -> Text:
        return 'action_check_user_language'

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        user_msg = tracker.latest_message.text
        language = TextBlob(user_msg)
        language = language.detect_language()
        return SlotSet('language', language)
