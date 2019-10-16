'''This game is the opposite of the original Guessing Game project (from Practice Python).
In this version, the user has a number in mind, and the computer has to keep guessing until it gets the correct number.
The computer will keep a log of how many attempts it made before it guessed correctly, and it will run off of the user's responses -
for example, "too high!" or "too low!"
'''
#First, import the random module
import random, math

def guessMyNumber():
    print("Please enter the range in which your number exists, and only input an integer.")
    try:
        startRange = int(input("I'm thinking of a number between 1 and... "))
        computerGuess = random.randint(1, startRange)
        randomPercentage = random.uniform(0.01, 1.0)
        rangeMin = 1
        rangeMax = startRange
        guessesCount = 0

        '''
        Now the computer has to start 'guessing' by suggesting random integers in that range.
        
        I have the program slowly tighten its range for possible integers by minusing one if the guess is too high from the rangeMax.
        If the program guesses too low, it sets the rangeMin to the computerGuess value, and same thing with rangeMax if the guess is too high.  So,
        between multiple "too high" and "too low" results the program eventually narrows it down more and more.  
        '''
        while True:
            print("\nComputer says, 'I think your number is {}'".format(computerGuess))
            guessesCount += 1
            print("The computer has made {} guesses".format(guessesCount))
            answer = input("To that I answer: ").lower()
            if answer == "too high":
                rangeMax = computerGuess
                computerGuess = random.randint(rangeMin, rangeMax)
                continue
            elif answer == "too low":
                rangeMin = computerGuess
                computerGuess = random.randint(rangeMin, rangeMax)
                continue
            elif answer == "that is right!":
                print("\nYay! The computer got it.  It took {} guesses".format(guessesCount))
                break
            else:
                print("Please either type 'too high', 'too low', or 'that is right!' as your response.")
    except ValueError:
        print("Fugg!  You just inputted the wrong data type.")
    except ZeroDivisionError:
        print("You just tried to divide by zero.  An angel loses its wings every time you divide by zero.")

if __name__ == '__main__':
    guessMyNumber()
