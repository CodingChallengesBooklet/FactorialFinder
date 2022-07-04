import math
from solution_benchmark import benchmark


# Using built-in function math.factorial
def find_factorial_with_math(x):
    return math.factorial(x)


# Alternative to recursion but without a total variable
def find_factorial_with_recursion2(x):
    return 1 if x == 0 else x * find_factorial_with_recursion2(x-1)


# Alternative to while loop using for loop
def find_factorial_with_loop2(x):
    total = 1
    for i in range(2, x+1):
        total = total * i
    return total


# Benchmarking alternative solutions
n = int(input("Enter a positive integer: "))
if n < 0:
    print("You have not entered a positive integer.")
else:
    print(f"Using math.factorial the factorial of {n} is {benchmark(lambda: find_factorial_with_math(n))}")
    print(f"Using recursion the factorial of {n} is {benchmark(lambda: find_factorial_with_recursion2(n))}")
    print(f"Using for loop the factorial of {n} is {benchmark(lambda: find_factorial_with_loop2(n))}")

