from pyfiglet import figlet_format as fig
from termcolor import colored
import requests
from random import choice

title = fig("Dad Joke 3000")
title = colored(title, color="magenta")
print(title)
topic = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": topic}
).json()

num_jokes = res["total_jokes"]
results = res["results"]

if num_jokes > 1:
    print(f"I found {num_jokes} about {topic}. Here is one: ")
    print(choice(results)['joke'])
elif num_jokes == 1:
    print(f"There is one joke about {topic}")
    print(results[0]['joke'])
else:
    print(f"Sorry, couldn't find the joke with your term: {topic}")
