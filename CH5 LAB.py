"""
Program: sentence generator.py
Marvick Felix
This program generates sentences using grammar and simple vocab and prints them.
"""
import random

prepositions = ("WITH", "BY")
articles = ("A", "THE")
nouns = ("DOG", "MOUSE", "CAR","KEYBOARD")
verbs = ("RAN","SAW","LEFT")

def sentence():
    return nounPhrase()+ " " + verbPhrase()

def nounPhrase():
    return random.choice(articles)+" " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase() 

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number): print(sentence())
if __name__ == "__main__":
    main()
