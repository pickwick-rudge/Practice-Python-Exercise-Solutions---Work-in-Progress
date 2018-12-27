'''Exercise 11: Check Primality Functions'''

'''Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.'''

def main():
    try:
        prompt = int(input("Please enter a number: "))
        #Generate a list comprehension that says to add to the list if the prompt is cleanly divisible by x
        #E.g., for 13, 13 % 13 and 13 % 1 will be the only two combinations between 1-13 that will cleanly divide
        prime_or_not = [x for x in range(1,prompt+1) if all(prompt % x == 0 for y in range(prompt))]
        #If the length of the list is greater than two, it's not a prime number (because it can be divided without remainder by other numbers besides one and itself)
        if len(prime_or_not) > 2:
            print("This is not a prime number.")
            print(prime_or_not)
        #Otherwise, it's prime
        else:
            print("This is a prime number.")
            print(prime_or_not)
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("Please stop trying to divide by zero.")
    except Exception:
        print("Oops!  Something else seems to have gone haywire.")

if __name__ == '__main__':
    main()
