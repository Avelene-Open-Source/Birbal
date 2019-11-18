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
        book_genre_type = tracker.get_slot('book_slot_value')
        if book_genre_type != 'Others':
            if book_genre_type == "Avelene's Choice":
                book_details = fetch_books_avelene_choice()
                dispatcher.utter_message('These are the best books I have found:\n{}'.format(book_details))
            else:
                book_details = fetch_books_categorywise(book_genre_type)
                dispatcher.utter_message('These are the best books I have found:\n{}'.format(book_details))
            return [FollowupAction('action_listen')]
        elif book_genre_type == "Others":
            return [FollowupAction('action_listen')]


class ActionSearchBook(Action):

    def name(self) -> Text:
        return 'action_search_book'

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        book_name = tracker.latest_message['text']
        book_details = fetch_books_user_search(book_name)
        dispatcher.utter_message('These are the details of the book you are looking for:\n{}'.format(book_details))
        return [SlotSet('search_book_name', book_name), FollowupAction('action_listen')]
