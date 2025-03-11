import os

"""
Sets up the Electric Meatball environment in an oppinionated way based on the default
configuration.
"""

gpt_answers = "gpt_answers"
gpt_chats = "gpt_chats"
http_req_dumps = "http_req_dumps"
img_dumps = "img_dumps"

file = open("user_prompt.txt", "w+")

os.makedirs(gpt_answers, exist_ok=True)
file = open(gpt_answers + "/" + "gpt_answers.txt", "w+")

os.makedirs(gpt_chats, exist_ok=True)
file = open(gpt_chats + "/" + "gpt_chat.json", "w+")

os.makedirs(http_req_dumps, exist_ok=True)
file = open(http_req_dumps + "/" + "http_req_dump.txt", "w+")

os.makedirs(img_dumps, exist_ok=True)
file = open(img_dumps + "/" + "img_dump.txt", "w+")

