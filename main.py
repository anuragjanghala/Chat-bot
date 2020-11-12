import json
import random
import tensorflow
import tflearn
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


with open("intents.json") as file:
    data = json.load(file)

print(data['intents'])

words = []
labels = []
docs = []

for intent in data['intents']:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)

    if intent['tag'] not in labels:
        labels.append(intent["tag"])
