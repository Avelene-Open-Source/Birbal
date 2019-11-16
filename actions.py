from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from utils import *

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


class ActionReadBook(Action):

    def name(self) -> Text:
        return 'action_read_book'

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        book_names = ''
        book_type = tracker.get_slot('book_slot_value')
        if book_type not in ["Avelene's Choice", 'Other']:
            book_names = fetch_books_categorywise(book_type)
        else:
            if book_type == "Avelene's Choice":
                book_names = fetch_books_avelene_choice()
        print('>>>>>>>>>>>>>', book_names)
        dispatcher.utter_message('These are the best books I have found:\n{}'.format(book_names))
