'''05 List Overlap'''

'''Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1) Randomly generate two lists to test this
2) Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

#I'll begin with the extra credit and randomly generate two lists. =)
import random
list_a = [random.randint(1,21) for x in range(10)]
list_b = [random.randint(1,21) for x in range(10)]

#Next, initialize an empty list to hold the numbers in common between both lists (if any) ->
list_in_common = []

#Loop through list_a, then say that if that number is in list_b as well, AND if it's not already in list_in_common, append it
#to list_in_common.
for num in list_a:
    if num in list_b and num not in list_in_common:
        list_in_common.append(num)

#Finally, print all three lists as proof that it works as advertised.
print(list_a)
print(list_b)
print(list_in_common)
