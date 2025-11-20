import random


def cardGuess():
    CardValue = random.randint(1, 11)
    print("Guess Card...please....")
    return CardValue


def startgame():
    print('Welcome to the card guessing game!')
    print('The objective here is to get the card you filp the closest to the number that was chosen')
    ourGuess = cardGuess()
    theiGuess = cardGuess()
    print("You rolled a " + str(cardGuess))
    print("House rolled a " + str(cardGuess))
    print('The Card was' + str(cardGuess))
    if ourGuess == cardGuess:
        print('You win!')
    elif theiGuess == cardGuess:
        print('They win!')
    else:
        print('You both lose!')

startgame()