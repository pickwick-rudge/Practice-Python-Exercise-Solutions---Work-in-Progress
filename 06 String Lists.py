'''06 String Lists'''

'''Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

'''There are apparently many ways to reverse a string, and I only employed one of them here.
This program asks for a string, then tests to see if it actually is a word (although numbers could also be contained in a string, so this is a little messy).
It then creates an empty string, then loops through each letter of the input, inserting the letter before the previous letter.
Both strings are compared, and if they're the same, the input string was a palindrome.  If not, it's not.'''

def main():
    while True:
        give_me_something = input('Please input a string, and I\'ll test to see if it\'s a palindrome or not: ')
        if give_me_something.isalpha():
            reversed = ''
            for letter in give_me_something:
                reversed = letter + reversed
            if give_me_something.lower() == reversed.lower():
                print(give_me_something.capitalize() + ' is a palindrome.')
                break
            else:
                print(give_me_something.capitalize() + ' is not a palindrome.')
                break
        else:
            print("Ups! Please input a string!  No numbers, ya cheater!")
            continue

if __name__ == '__main__':
    main()
