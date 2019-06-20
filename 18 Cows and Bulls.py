"Programmed by Michael Kich"

"""This is a program that will play the 'Cows and Bulls' game with the user.

The program randomly generates a four-digit number.  The user then has to guess
which number was generated, and inputs a guess.  For each guess, a counter
increments.  Each digit in random_number is measured against each digit in guess.
If the digit in each is the correct digit and is also at the correct index value,
then the user gets a cow.  If the digit is in random_number, but is at another index location,
then the user gets a bull.
"""
import random
import sys

guess_count = 0 #Counter to keep track of user guesses

def main():
    while True:
        cow_count = 0 #Counter to keep track of cows
        bull_count = 0 #counter to keep track of bulls

        print('Welcome to the Cows and Bulls Game!')
        random_number = str(random.randint(1000,9999)) #generate a random four-digit number
        print('Your randomly generated number is %s\n' % random_number) #For troubleshooting

        try:
            guess = input('Please guess a four-digit number: \n') #Accept guess
            if len(guess) < 4 or len(guess) > 4:
                raise ValueError
            global guess_count #make local function variable guess_count global
            guess_count += 1 #...then increment
            print('You have guessed', guess_count, 'times so far.\n')

            suss_out_the_nums(guess, random_number, guess_count, cow_count, bull_count)

            while True: #Ask user if they'd like to go again, respond accordingly
                go_again = input('Would you like to play again? Y for yes and N for no.\n')
                if go_again.isalpha() and go_again.upper() == 'Y':
                    main()
                elif go_again.isalpha() and go_again.upper() == 'N':
                    print('Okay, thanks for playing my game!')
                    sys.exit()
                else:
                    print('Please enter Y or N for yes or no')
        except KeyboardInterrupt:
            print('Looks like someone performed a keyboard interrupt.\n')
        except ValueError:
            print('Ahh ahh ahh, input a four-digit number!\n')
        except:
            print('Hmm, something went wrong...')
            print('Oh woops, the exception',sys.exc_info()[0],'happened and the program crashed.\n')
        finally:
            sys.exit() #Not the perfect solution I'd prefer,
            #because it raises the SystemExit exception, but at least it terminates
            #the program

def suss_out_the_nums(guess, random_number, guess_count, cow_count, bull_count):
    for num in range(len(random_number)): #For each number in the range of the length of the random number...
        if guess[num] == random_number[num]: #If the num at that index is equal to the num at equivalent index in random_number
            print('Yay!  You guessed the correct digit at index - have a cow.')
            cow_count += 1
            print('You currently have %s cows and %s bulls\n' % (cow_count, bull_count))
        elif guess[num] != random_number[num] and guess[num] in random_number: #If it's not, but the digit guessed *is* in the random_number somewhere
            print('Well, it\'s the right digit in the wrong place - have a bull.')
            bull_count += 1
            print('You currently have %s cows and %s bulls\n' % (cow_count, bull_count))
        elif guess[num] != random_number[num] and guess[num] not in random_number: #And finally, if the digit's not in the random_number at all
            print('Oops! %s does not appear in this randomly generated number.' % guess[num])
            print('You currently have %s cows and %s bulls\n' % (cow_count, bull_count))

    if guess == random_number:
        print("Hoorah!  You win!")
        guess_count = 0
        cow_count = 0
        bull_count = 0
    else:
        print('Hmm, you guessed %s and the correct number is %s.' % (guess, random_number))

if __name__ == '__main__':
    main()
