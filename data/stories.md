## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## story 01
* greet
  - utter_greet

## story 02
* goodbye
  - utter_goodbye

## story 05
* default
  - utter_default

## story 06
* acquaintance
  - utter_acquaintance

## story 07
* age
  - utter_age

## story 08
* annoying
  - utter_annoying

## story 09
* answer_my_question
  - utter_answer_my_question

## story 10
* frustration
  - utter_frustration

## story 11
* be_clever
  - utter_be_clever

## story 12
* beautiful
  - utter_beautiful

## story 13
* birth_date
  - utter_birth_date

## story 14
* boring
  - utter_boring

## story 15
* boss
  - utter_boss

## story 16
* busy
  - utter_busy

## story 17
* can_you_help
  - utter_can_you_help

## story 18
* chatbot
  - utter_chatbot

## story 19
* clever
  - utter_clever

## story 20
* crazy
  - utter_crazy

## story 21
* fired
  - utter_fired

## story 22
* funny
  - utter_funny

## story 23
* good_bot
  - utter_good_bot

## story 24
* happy
  - utter_happy

## story 25
* hobby
  - utter_hobby

## story 26
* hungry
  - utter_hungry

## story 27
* marry_user
  - utter_marry_user

## story 28
* my_friend
  - utter_my_friend

## story 29
* occupation
  - utter_occupation

## story 30
* origin
  - utter_origin

## story 31
* ready
  - utter_ready

## story 32
* real
  - utter_real

## story 33
* residence
  - utter_residence

## story 34
* right
  - utter_right

## story 35
* sure
  - utter_sure

## story 36
* talk_to_me
  - utter_talk_to_me

## story 37
* there
  - utter_there

## story 38
* bad
  - utter_bad

## story 39
* good
  - utter_good

## story 40
* no_problem
  - utter_no_problem

## story 41
* thank_you
  - utter_thank_you

## story 42
* welcome
  - utter_welcome

## story 43
* well_done
  - utter_well_done

## story 44
* hold_on
  - utter_hold_on

## story 45
* hug
  - utter_hug

## story 46
* i_do_not_care
  - utter_i_do_not_care

## story 47
* sorry
  - utter_sorry

## story 48
* what_do_you_mean
  - utter_what_do_you_mean

## story 49
* wrong
  - utter_wrong

## story 50
* ha_ha
  - utter_ha_ha

## story 51
* wow
  - utter_wow

## story 52
* goodevening
  - utter_goodevening

## story 53
* goodmorning
  - utter_goodmorning

## story 54
* goodnight
  - utter_goodnight

## story 55
* greetings_how_are_you
  - utter_greetings_how_are_you

## story 56
* greetings_nice_to_meet_you
  - utter_greetings_nice_to_meet_you

## story 57
* greetings_nice_to_see_you
  - utter_greetings_nice_to_see_you

## story 58
* greetings_nice_to_talk_to_you
  - utter_greetings_nice_to_talk_to_you

## story 59
* greetings_whatsup
  - utter_greetings_whatsup

## story 60
* user_angry
  - utter_user_angry

## story 61
* user_back
  - utter_user_back

## story 62
* user_bored
  - utter_user_bored

## story 63
* user_busy
  - utter_user_busy

## story 64
* user_can_not_sleep
  - utter_user_can_not_sleep

## story 65
* user_does_not_want_to_talk
  - utter_user_does_not_want_to_talk

## story 66
* user_excited
  - utter_user_excited

## story 67
* user_going_to_bed
  - utter_user_going_to_bed

## story 68
* user_good
  - utter_user_good

## story 69
* user_happy
  - utter_user_happy

## story 70
* user_has_birthday
  - utter_user_has_birthday

## story 71
* user_here
  - utter_user_here

## story 72
* user_joking
  - utter_user_joking

## story 73
* user_likes_agent
  - utter_user_likes_agent

## story 74
* user_lonely
  - utter_user_lonely

## story 75
* user_looks_like
  - utter_user_looks_like

## story 76
* user_loves_agent
  - utter_user_loves_agent

## story 77
* user_misses_agent
  - utter_user_misses_agent

## story 78
* user_needs_advice
  - utter_user_needs_advice

## story 79
* user_sad
  - utter_user_sad

## story 80
* user_sleepy
  - utter_user_sleepy

## story 81
* user_testing_agent
  - utter_user_testing_agent

## story 82
* user_tired
  - utter_user_tired

## story 83
* user_waits
  - utter_user_waits

## story 84
* user_wants_to_see_agent_again
  - utter_user_wants_to_see_agent_again

## story 85
* user_wants_to_talk
  - utter_user_wants_to_talk

## story 86
* user_will_be_back
  - utter_user_will_be_back

## story read_book
* read_book
  - utter_read_book

## story 86
* okay
  - utter_okay

## story 87
* confirmation
  - utter_okay

## interactive_story_1
* read_book{"read_book": "book"}
    - utter_read_book
* book_slot_value{"book_slot_value": "Avelene's Choice"}
    - slot{"book_slot_value": "Avelene's Choice"}
    - action_read_book

## interactive_story_1
* read_book{"read_book": "book"}
    - utter_read_book
* book_slot_value{"book_slot_value": "Avelene's Choice"}
    - slot{"book_slot_value": "Avelene's Choice"}
    - action_read_book

## interactive_story_1
* read_book{"read_book": "book"}
    - utter_read_book
* book_slot_value{"book_slot_value": "Fiction"}
    - slot{"book_slot_value": "Fiction"}
    - action_read_book

## interactive_story_1
* read_book
    - utter_read_book
* book_slot_value{"book_slot_value": "Crime"}
    - slot{"book_slot_value": "Crime"}
    - action_read_book

## interactive_story_1
* read_book{"read_book": "book"}
    - utter_read_book
* book_slot_value{"book_slot_value": "Others"}
    - slot{"book_slot_value": "Others"}
    - action_read_book
    - followup{"name": "action_listen"}
* boring
    - action_search_book

## interactive_story_1
* read_book{"read_book": "book"}
    - utter_read_book
* book_slot_value{"book_slot_value": "Others"}
    - slot{"book_slot_value": "Others"}
    - action_read_book
    - followup{"name": "action_listen"}
* greet
    - action_search_book
    - slot{"search_book_name": "Sherlock Holmes"}
    - followup{"name": "action_listen"}

## interactive_story_1
* read_book{"read_book": "book"}
    - utter_read_book
* book_slot_value{"book_slot_value": "Others"}
    - slot{"book_slot_value": "Others"}
    - action_read_book
    - followup{"name": "action_listen"}
* bad
    - action_search_book
    - slot{"search_book_name": "Rich Dad Poor Dad"}
    - followup{"name": "action_listen"}
