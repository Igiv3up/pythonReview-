import random

def diceRoll():
    diceValue = random.randint(1,6)
    return diceValue

def startGame():
    print('Welcome to Dice Roll! its your roll vs theirs')
    print("This program is now on gitHub!")
    ourRoll = diceRoll()
    theirRoll = diceRoll()
    print("You rolled a " + str(ourRoll))
    print("House rolled a " + str(theirRoll))
    if ourRoll == theirRoll:
        print('Draw')
    elif ourRoll > theirRoll:
        print('You win')
    else:
        print('You lose')


startGame()
