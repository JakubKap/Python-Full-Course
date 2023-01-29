import json
import os.path
from datetime import datetime
from urllib import request

import pyttsx3
import requests

import calculator
from joke import Joke
from phone import Phone

# calculator operations
print("Calculator operations results:")
print(calculator.add(2, 2))
print(calculator.subtract(2, 2))
print(calculator.divide(2, 2))
print(calculator.multiply(2, 3))

# Phone operations
iphone = Phone("IPhone 7+", 300)
samsung = Phone("Samsung S20", 1400)

print("\nPhone creations results:")
print(iphone)
print(samsung)

# Working with dates
print("\nDates examples:")
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

# Date formatting
print("\nFormatted date:")
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))

# File operations (w - writing, a - appending, r+ - reading and writing)
filename = "./data.csv"
file = open(filename, "w")
file.write("id, name, email\n")
file.write("1, Jakub, jk@gmail.com\n")
file.write("2, John, john@gmail.com\n")
file.close()

print("\nFile content:")
file = open(filename, "r")
for line in file:
    print(line)
file.close()

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"File {filename} does not exist")

# Fetching data from Internet
print("\nFetching data from Internet:")
response = request.urlopen("http://www.google.com")
print(response.getcode())
print(response.read())

# Fetching jokes from API
print("\nFetching jokes from API:")
url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(r.getcode())
response = requests.get(url)
jsonData = json.loads(response.text)
print(jsonData)

jokes = []
for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke = Joke(setup, punchline)
    jokes.append(joke)

print(f"\nGot {len(jokes)} jokes:")
for joke in jokes:
    print(joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("Punchline")
    pyttsx3.speak(joke.punchline)
