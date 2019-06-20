'''Code by: Michael Kich'''

'''
Password Generator challenge:

Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase letters,
numbers, and symbols. The passwords should be random, generating a new password
every time the user asks for a new password. Include your run-time code in a
main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.'''

import random, sys

def convert_list(list): #function to convert list into individual strings, then use .join() to link them up into a single entry
    s = [str(letter) for letter in list]
    password_string = "".join(s)
    return password_string

def main():
    while True:
        print("Time to create a password!  How strong would you like it to be?")
        print("Input the number of characters you would like your password to have, and one will be pseudo-randomly generated for you!\n")
        password_length = input()
        if password_length.isdigit():
            #Generate a list with a population provided as the first argument, and with the password length input as the second argument
            new_password = random.sample("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()", int(password_length))

            #Call the convert_list function to convert the password list into a single string, and print result to console
            print("Your new password is", convert_list(new_password),"\n")

            #Ask if user would like to generate another password
            print("Would you like to generate another?  'Y' for yes, 'N' for no.\n")
            go_again = input().upper()
            print()
            if go_again == 'Y':
                continue
            else:
                print("Thanks for using my program!  Goodbye!")
                sys.exit()
        else:
            print("Please input a valid length for your desired password.")
            continue

if __name__ == '__main__':
    main()
