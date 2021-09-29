"""
Luke Shafer
Radical Software, Fall 2021
Sept 23, 2021
python3
"""

import tweepy

from authorization_tokens import *

import random

phrase_list = ["Pride is not the opposite of shame, but its source. True humility is the only antidote to shame.",
"Sometimes the best way to solve a problem is to help others.", "I know you're not supposed to cry over spilled tea, but... it's just so sad.",
"Protection and power are overrated. I think you are to choose between happiness and love.",
"History is not always kind to its subjects.",
"Failure is the only oppurtunity to begin again.",
"Good times become good memories, but bad times make good lessons.",
"It is usually best to admit mistakes when they occur, and to seek to restore honor.",
"It is important to draw wisdom from many different places.",
"Who are you and what do YOU want?",
"Sharing tea with a fascinating stranger is one of life's true delights.",
"Hope is something you give yourself. That is the meaning of inner strength.",
"Destiny is a funny thing. You never know how things are going to work out.",
"A little help from others can be a great blessing.",
"Life happens wherever you are, whether you make it or not."
"Leaves from the vine, falling so slow. </3",
"You have light and peace inside of you.",
"Many things that seem threatening in the dark become welcoming when we shine light on them.",
"Follow your passion and life will reqard you.",
"At my age, there is really only one big surprise left, and I'd just as soon leave it a mystery.",
"There are reasons eavh of us are born. We have to find those reasons.",
"I was never angry with you. I was sad, because I was afraid you'd lost your way.",
"Understanding others, the other elements, the other nations, will help you become whole.",
"There is nothing wrong with letting people who love you, help you.",
"I always tried to tell you that Pai Sho is more than just a game."]
message = random.choice(phrase_list)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
