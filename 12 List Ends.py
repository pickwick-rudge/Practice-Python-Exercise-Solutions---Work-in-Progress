'''Exercise 12: List Ends'''

'''Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
 and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.'''

import random

def list_begins_and_ends(a):
    #Returns index zero and the index of the last number in the list (length of the list minus one, to compensate for zero-indexing)
    return [a[0], a[len(a)-1]]

def main():
    a = [random.randint(1,10) for x in range(10)]
    print(a)
    print(list_begins_and_ends(a))

if __name__ == '__main__':
    main()
