'''List Less Than Ten'''

'''Takes a list and writes a program that prints out all the elements of the list that are less than 5.'''

'Create a list from the randomizer function using a list comprehension.'
import random
aNewList = [random.randint(1,21) for x in range(11)]

'Print randomly generated list.'
print(aNewList)

'Initialize an empty list to append to.'
listLessThanFive = []
'For every number in the list, if it\'s less than 5, append to listLessThanFive.'
for number in aNewList:
    if number < 5:
        listLessThanFive.append(number)

'Print new list.'
print(listLessThanFive)
