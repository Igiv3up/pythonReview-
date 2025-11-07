import random

def cardGuess():
    CardValue = random.randint(1,11)
    return CardValue

def startgame ():
    print('Welcome to the card guessing game!')
    print('The objective here is to get the card you filp the closest to the number that was chosen')
    
