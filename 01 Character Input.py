'''01 Character Input'''

'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

'''I could make this program's output much more precise, but for now I just want to accomplish the stated goal
in the 'Practice Python' exercise.'''

def WhenWillITurn100():
    Difference = 100 - User_age
    print("Dear " + str(User_name) + ": " + "you are " + str(User_age) + " years old and you will turn 100 years old in " + str(Difference) + " years.")

while True:
    User_name = input("Please enter your name: ")
    User_age = input("Please enter your age: ")
    if User_name.isalpha() and User_age.isdigit():
        User_age = int(User_age)
        WhenWillITurn100()
        break
    else:
        print("Oops!  Please enter only alphanumeric characters for your name, and only integers for your age.")
        continue
