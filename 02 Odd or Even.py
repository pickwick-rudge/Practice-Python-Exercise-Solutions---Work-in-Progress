'''02 Odd or Even'''

'''Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.'''

def AnotherNumber():
    while True:
        goagain = input("Would you like to go again? ")
        if goagain.isalpha():
            if goagain == 'y':
                OddOrEven()
            elif goagain == 'n':
                print("Thank you for using my program!")
                exit()
            else:
                print("Please input either 'y' or 'n'.")
                continue
        else:
            print("Please input either 'y' or 'n'.")
            continue

def OddOrEven():
    while True:
        number_input = input("Please input a number: ")
        if number_input.isdigit():
            number_input = int(number_input)
            if number_input % 2 == 0:
                print("The number " + str(number_input) + " is even.")
                AnotherNumber()
            else:
                print("The number " + str(number_input) + " is odd.")
                AnotherNumber()
        else:
            print("Please input an integer.")
            continue

if __name__ == '__main__':
    OddOrEven()
