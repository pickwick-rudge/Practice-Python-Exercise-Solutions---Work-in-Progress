'''Write a program (function!) that takes a list and
returns a new list that contains all the elements of the first
list minus all the duplicates.'''

import random

#Accomplish the task with a for loop and two lists...
def RemoveDups_Lists():
    #First, create a random list
    list_a = [random.randint(1,10) for x in range(10)]

    #Then, create a second list that removes all of the duplicates
    list_b = []
    duplicate_counter = 0

    for entry in list_a:
        if entry not in list_b:
            list_b.append(entry)
        else:
            duplicate_counter += 1

    #Print out the second list along with the number of duplicates exempted
    print("Accomplish the task first with two lists ->")
    print(list_a)
    print(list_b)
    print("The number of duplicates detected is", duplicate_counter)

#...or, accomplish the same task with a set
def RemoveDups_Sets():
    #Create an empty set
    set_a = set()

    #Pseudo-randomly generate ten integers and add them to the set.
    #The set will automatically filter out duplicates, so the conditionals
    #from the previous function aren't necessary

    #The set will only print with ten integers if all of the integers are unique
    for x in range(10):
        set_a.add(random.randint(1,10))

    print("\nAccomplish the task next with a set ->")
    print(set_a)

def main():
    RemoveDups_Lists()
    RemoveDups_Sets()


if __name__ == '__main__':
    main()
