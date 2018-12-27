'''04 Divisors'''

'''Creates a program that asks the user for a number and then prints out a list of all the divisors of that number. '''

#Function that asks the user whether they would like to input another number.'
def goAgain():
    while True:
        anotherNum = input('Would you like to enter another number in? ')
        if anotherNum.isalpha() and anotherNum == 'y' or 'n':
            if anotherNum == 'y':
                Main()
            elif anotherNum == 'n':
                print("Thank you for using my program!")
                exit()
        else:
            #Don't know why I can't get the following line of code to work...
            print("Please enter either 'y' or 'n'.")
            continue


'''Main function takes an inputted number, checks to make sure it\'s an int, then creates a list
for the range between 1 and the user's number (plus one, because it's a range).

It then appends every number to the divisors list that divides with the user number without remainder.
'''
def Main():
    while True:
        user_number = input('Please enter a number: ')
        if user_number.isdigit():
            user_number = int(user_number)
            number_range = [x for x in range(1, user_number + 1)]
            divisors_list = []
            for num in number_range:
                if user_number % num == 0:
                    divisors_list.append(num)
            print(divisors_list)
            goAgain()
        else:
            print('Please enter an integer.')
            continue

if __name__ == '__main__':
    Main()
