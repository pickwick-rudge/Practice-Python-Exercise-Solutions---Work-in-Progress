'''
This implements a function that takes three input variables
and ferrets out the max value without resorting to python's
built-in max() function
'''

import random

def maximizeMe():
    #Interesting thing here - set objects create unique values, but they don't support indexing
    #So, I needed to first convert the list to a set, then back again to a list
    variablesList = [random.randint(1,100) for x in range(3)]
    maxer = variablesList[0]

    #For a descending order list:
    for i in range(len(variablesList)):
        for j in range(0, len(variablesList)-i-1):
            if variablesList[j] < variablesList[j+1]:
                variablesList[j], variablesList[j+1] = variablesList[j+1], variablesList[j]
    maxer = variablesList[0]
    print(variablesList)
    print(maxer)

    #For an ascending order list:
    for i in range(len(variablesList)):
        for j in range(0, len(variablesList)-i-1):
            if variablesList[j] > variablesList[j+1]:
                variablesList[j], variablesList[j+1] = variablesList[j+1], variablesList[j]
    maxer = variablesList[-1]
    print(variablesList)
    print(maxer)

maximizeMe()

'''
I decided to go about this by coding a basic bubble sort algorithm that sorts in ascending or descending order, then
just prints either the initial or the final item in the list (which will necessarily be the max of the three numbers generated).
'''
