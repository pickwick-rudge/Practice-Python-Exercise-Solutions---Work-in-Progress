'''Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string, except with
the words in backwards order. For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.'''

def main():
    #Have the user input a string
    teststring = input("Please enter something, preferably a full sentence: ")
    print("\nInput string: " + teststring)

    #Now, split the string on every whitespace
    result = teststring.split(" ")

    #Use reverse() to reverse the entries in the 'result' list
    result.reverse()

    #Initialize an empty string and append the contents of 'result' to it
    finalstring = ""
    for word in result: #For each word, if it contains the following four punctuation characters at the end of the word...
        if '.' in word or '!' in word or ',' in word or '?' in word:
            finalstring += word.rstrip('.!,?') + " " #Strip them off
        else:
            finalstring += word + " " #Otherwise, just add the word to the final string
    print("\nReversed string: " + finalstring.capitalize())

if __name__ == '__main__':
    main()
