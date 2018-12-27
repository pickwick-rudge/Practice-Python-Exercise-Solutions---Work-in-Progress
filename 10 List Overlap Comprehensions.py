'''Exercise 10: List Overlap Comprehensions'''

'''Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common
between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Write this in one line of Python using at least one list comprehension.
(Hint: Remember list comprehensions from Exercise 7).'''

def main():
	#Import the random module and create two lists with ints between 1-100 and in range 20.
	#This was bonus in the exercise
	import random

	a = [random.randint(1,100) for x in range(20)]
	b = [random.randint(1,100) for x in range(20)]
	#Next, create list c using the set operator in order to get distinct results (no duplicates)
	#The set operator is new for me at this point
	c = [x for x in set(a) if x in b]

	#I then use the sorted() function just to order the list results for all three lists
	print(sorted(a))
	print()
	print(sorted(b))
	print()
	print(sorted(c))

if __name__ == '__main__':
	main()
