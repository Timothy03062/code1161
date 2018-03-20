"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""


from exercise1 import not_number_rejector
from exercise1 import super_asker
import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    marge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    def advancedGuessingGame():
        print("Welcome to the guessing game!")
    i=input("Set a lower bound: ")
    while True:
        try:
            i= int(i)
            break
        except ValueError:
            i=input('Set a lower bound again: ')
            continue
    s=input("Set a higher bound: ")
    while True:
        try:
            s = int(s)
            while True:
                if int(s)>int(i):
                    break
                else:
                    s=input("The number should bigger than the low bound, set again: ")
            break
        except ValueError:
            s=input('Set a higher bound again: ')
            continue
    print ("Now, guess a number between "+str(i)+" and "+str(s))
    actualNumber = random.randint(int(i), int(s))
    guessed = False
    while not guessed:
        guessedNumber = input("guess a number: ")
        while True:
            try: 
                guessedNumber=int(guessedNumber)
                break
            except ValueError:
                guessedNumber=input('You should enter a number to guess: ')
                continue
        print("you guessed {},".format(guessedNumber),)
        if int(guessedNumber) == int(actualNumber):
            print("you got it!! It was {}".format(actualNumber))
            guessed = True
        elif int(guessedNumber) < int(actualNumber):
            print("too small, try again ")
        else:
            print("too big, try again  ")  
    return "You got it!"


if __name__ == "__main__":
    advancedGuessingGame()