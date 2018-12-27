'''Exercise 13: Fibonacci'''

'''Write a program that asks the user how many Fibonnaci numbers to generate and
then generates them. Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers
where the next number in the sequence is the sum of the previous two numbers in the
sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)'''

def Fibonacci():
    try:
        how_many_numbers = int(input("How many Fibonacci numbers would you like to generate? "))
        index = 1
        if how_many_numbers == 0:
            Fibonacci = []
        elif how_many_numbers == 1:
            Fibonacci = [1]
        elif how_many_numbers == 2:
            Fibonacci = [1,1]
        elif how_many_numbers > 2:
            Fibonacci = [1,1]
            while index < (how_many_numbers - 1):
                Fibonacci.append(Fibonacci[index] + Fibonacci[index-1])
                index += 1
        print(Fibonacci)
    except ValueError:
        print("Please enter an integer value for how many Fibonacci numbers you'd \
        like to generate.")
    except Exception:
        print("Well this is embarrassing. =(")

if __name__ == '__main__':
    Fibonacci()
