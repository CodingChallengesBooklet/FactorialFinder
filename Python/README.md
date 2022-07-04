# Factorial Finder in Python
In this code challenge we write a program that finds the factorial of a positive integer in the Python programming language.

## Problem
The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zeo, 0, is defined as being 1. Solve this using both loops and recursion.

## Solution
As the problem specifies we are trying to find the factorial of a positive integer. 
A factorial is the product of all numbers between n and 0. For example, if n is 10 then the factorial of n would be 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800. 
The challenge also states we must solve it using both loops and recursion.

### Solving the factorial with loops
Python has multiple kinds of loops including both while loops and for loops. Below is the solution shown in solution.py using a while loop.
1. We first take the parameter `x` which is going to be the positive integer from our user. 
2. We define the variable `total` with the value 1. This stores our final value.
3. We create a while loop that checks if x is above 0 and if not it will stop.
4. Within the loop we multiply the `total` by `x`, and subtract `x` by 1.
5. After the loop has finished we return the total.
```python
def find_factorial_with_loop(x):
    total = 1
    while x > 0:
        total = total * x
        x = x - 1
    return total
```

### Solving the factorial with recursion
Using recursion we call our function from within our function.
Recursive functions allow us to write easier to understand and compact code.
When a beginner first encounters recursion it can be hard to understand, so I'll explain this slowly.
1. We declare our function with two arguments, `x` which is our positive integer, and `total` we will use to store the final value (default value to 1).
2. We check if `x` is 0 and if it is we will return the `total`.
3. Otherwise, if `x` is not 0 we will call our own function from within, but we will modify the arguments.
   1. `x` is changed to `x-1` this will reduce `x` by one every time we call the function, which is when x is not 0.
   2. `total` is changed to `total*x` this will multiply `total` by `x` every time we call the function.
4. This continues until `x` is reduced to 0 in which case we will return the `total`.
```python
def find_factorial_with_recursion(x, total=1):
    return total if x == 0 else find_factorial_with_recursion(x-1, total*x)
```
*NOTE: Python has a recursion depth limit. This means Python will not recurse a function past a limit (995 recursions). This means using the recursion method Python cannot find the factorial of numbers of 996 or more.*

## Advanced
In the `Python` folder there is a `solution_advanced.py`. 
The solutions inside this file are alternatives to the solutions found in `solution.py`. 
If you wish to find the factorial in Python in the future I would recommend you use the built-in function `factorial` found in the `math` module. Example of use below.
```python
import math
print(math.factorial(10)) # Prints the factorial of 10
```
The python `math` module is not written in Python but in the C programming language which makes this solution the fastest out of all the solutions within this repository.
This is because the C programming language is faster and more efficient than Python.

## Benchmarking
In the `Python` folder there are three Python files: `solution.py`, `solution_benchmark.py`, and `solution_advanced.py`. 
The benchmark version of the solution will show how long (in nanoseconds) it takes for the factorial to be found. This allows you to see how fast each different version of finding the factorial is the fastest. Below is the timings I recorded on my computers. <br>

| Position | Score (nanoseconds) | Version        | n (integer provided) | file                 |
|:--------:|---------------------|----------------|----------------------|----------------------|
|    1     | 184317              | math.factorial | 800                  | solution_advanced.py |
|    2     | 887906              | while loop     | 800                  | solution.py          |
|    3     | 1496771             | for loop       | 800                  | solution_advanced.py |
|    4     | 2996144             | recursion      | 800                  | solution_advanced.py |
|    5     | 4874392             | recursion      | 800                  | solution.py          |

<br>
*NOTE: `soltuion_benchmark.py` contains only the benchmark code for `solution.py`, `solution_advanced.py` will benchmark itself on its own.*
