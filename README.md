# Factorial Finder
In this code challenge we write a program that finds the factorial of a positive integer.

## Problem
The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zeo, 0, is defined as being 1. Solve this using both loops and recursion.

## Solution
<i>NOTE: The solution explained here is a generalised solution. If you want a language-specific solution read the explanation in the language folder of your choice.</i>
<br>
As the problem specifies we are trying to find the factorial of a positive integer. 
A factorial is the product of all numbers between n and 0. For example, if n is 10 then the factorial of n would be 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800. 
The challenge also states we must solve it using both loops and recursion.

### Solving the factorial with loops
To find the factorial of n we can create a loop that multiplies a variable (we'll call x) by n on every loop through.
We then subtract n by 1 on every loop to decrease n.
We then check if n is below 1.
Below is pseudocode used to find the factorial of 10. 
```
n = 10 
x = 1
LOOP
   IF n < 1 THEN
      STOP LOOP
   ELSE
      x = x * n
      n = n - 1
END
```

### Solving the factorial with recursion
Using recursion we call our function from within our function.
Recursive functions allow us to write easier to understand and compact code.
In the example below we declare a function call `f` that takes the argument `n`.
Within `f` we check if `n` is below 1, if so we return 0, otherwise we return `n * f(n-1)`.
``` 
f = FUNCTION (n)
   IF n < 1 THEN
      0
   ELSE
      n * f(n-1)
      
f(10)
```