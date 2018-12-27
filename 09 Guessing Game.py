'''Guessing Game One'''

'''Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.'''

#Start by importing the random module and generating a random integer
#The simplest way to ensure that the number remains the same for the duration
#of the program is to place it outside of either of the functions

#If it's placed inside of main(), a new random integer is generated every time goagain() calls main()
import random
random_number = random.randint(1,9)

#Also import sys, to be able to call the sys.exit() function
import sys

#goagain() handles checking whether the user wants to guess again, and only accepts 'y' or 'n'
def goagain():
    while True:
        guess_again = input('Aww, not this time.  Care to guess again? ')
        if guess_again.isalpha() and (guess_again == 'y' or guess_again == 'n'):
            if guess_again == 'y':
                main()
            elif guess_again == 'n':
                print('Thanks for playing this guessing game!')
                #Calling anything other than break here (such as exit(), or even sys.exit()) will generate a SystemExit exception
                break
        else:
            print('Please enter either (y)es or (n)o.')
            continue



def main():
    try:
        your_guess = int(input('Please guess a number between 1 and 9: '))
        if your_guess == random_number:
            print('Your guess is correct! The number was ' + str(random_number) + '.')
            return
        else:
            goagain()
    except ValueError:
        print('Woops! You have to enter in an integer.')
    except KeyboardInterrupt:
        print('You must have pressed the keyboard interrupt key (CTRL+C or delete.)')
    except SystemExit:
        print('Python doesn\'t like it when you call exit() on the program.')
    except:
        print('You committed some other sort of error, it seems.')
    finally:
        #Interestingly enough, I can either call sys.exit() with 0 as an argument (which the system interprets as a clean exit) or just leave it blank,
        #in which case 'none' is interpreted in the same way as 0 would be
        sys.exit(0)


if __name__ == '__main__':
    main()
