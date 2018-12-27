'''Rock Paper Scissors'''

'''Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), \
compare them, print out a message of congratulations to the winner, and ask \
if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
'''

print("Welcome to Rock Paper Scissors!")
print("Please choose rock, paper, or scissors.")
print()

#After the initial welcome messages, I define two functions that contain the game
#Because this is supposed to be a two-player game and not single-player vs. computer,
#it's not necessary to import the random module

#Playagain() controls whether the user(s) would like to play again or not after every round
#If not, it exits the program
def playagain():
    while True:
        do_I_play_or_do_I_go_now = input('Would you like to play again? ').lower()
        if do_I_play_or_do_I_go_now.isalpha() and do_I_play_or_do_I_go_now == 'y' or do_I_play_or_do_I_go_now == 'n':
            if do_I_play_or_do_I_go_now == 'y':
                main()
            elif do_I_play_or_do_I_go_now == 'n':
                print('Okay, thanks for playing!')
                exit()
        else:
            print('Please input either (y)es or (n)o.')
            continue


#Here in the main module is the meat of the program
#It checks the input to make sure it's alphabetic, then goes through the conditional statements to see who wins, or if
#it's a tie

#Notice that both functions use while-loops to maintain a continuous game -
#this would be difficult to do with try/except blocks, although that would catch errors better.  
def main():
    while True:
        player_one = input("Player One, please choose: ").lower()
        player_two = input("Player Two, please choose: ").lower()
        if player_one.isalpha() and player_two.isalpha():
            if player_one == 'rock':
                if player_two == 'rock':
                    print('Rock on rock - go again.')
                    continue
                elif player_two == 'paper':
                    print('Paper beats rock. You lose!')
                    playagain()
                elif player_two == 'scissors':
                    print('Rock beats scisssors.  You win!')
                    playagain()
                else:
                    print('Please choose only rock, paper, or scissors.')
                    continue
            elif player_one == 'paper':
                if player_two == 'rock':
                    print('Paper beats rock.  You win!')
                    playagain()
                elif player_two == 'paper':
                    print('Paper on paper - go again.')
                    continue
                elif player_two == 'scissors':
                    print('Scissors cuts paper.  You lose!')
                    playagain()
                else:
                    print('Please choose only rock, paper, or scissors.')
                    continue
            elif player_one == 'scissors':
                if player_two == 'rock':
                    print('Rock breaks scissors.  You lose!')
                    playagain()
                elif player_two == 'paper':
                    print('Scissors cuts paper.  You win!')
                    playagain()
                elif player_two == 'scissors':
                    print('Scissors on scissors - go again')
                    continue
                else:
                    print('Please choose only rock, paper, or scissors.')
                    continue
            else:
                print('Please choose only rock, paper, or scissors.')
                continue
        else:
            print('Please input only alphabetic characters!')
            continue

if __name__ == '__main__':
    main()
