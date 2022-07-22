# Factorial Finder in Rust
In this code challenge we write a program that finds the factorial of a positive integer in the Rust programming language.

## Problem
The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and the factorial of zeo, 0, is defined as being 1. Solve this using both loops and recursion.

## Solution
As the problem specifies we are trying to find the factorial of a positive integer. 
A factorial is the product of all numbers between n and 0. For example, if n is 10 then the factorial of n would be 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 3628800. 
The challenge also states we must solve it using both loops and recursion.

### Solving the factorial with loops
Rust has different kinds of looping but the best kind of loop for our situation is a `while` loop.
This loops lets us check if a condition is true to break the loop, in our case, we check if `f` is above `1`.
1. Create a function that takes the mutable i64 parameter `f` and returns an 64-bit integer.
2. loop until `f` is `0` or below 
   1. multiply the sum (default to 1) by `f`
   2. subtract `f` by `1` (decreasing the count until `f` is 0)
3. Return the sum
This simulates the process of factorial by multiplying the sum by every digit between `f` and `0`.
```rust
// Simple looping algorithm
fn factorial_loop(mut f: i64) -> i64 {
    // sum is 1 so if f is 0 the function returns 1
    let mut sum: i64 = 1;

    // Multiplying the sum by f and subtracting f by 1 every loop
    while f > 0 {
        sum *= f;
        f -= 1;
    }

    return sum;
}
```

### Solving the factorial with recursion
Using recursion can make our code shorter and easier to understand. In this technique, we call the function within it's self usually with altered arguments.
1. Create a function that takes the mutable i64 parameter `f` and returns an 64-bit integer.
2. if `f` is 0 or below 0 we return 1
3. otherwise we return `f` multiplied by the function by with `f` reduced by 1
```rust
// Recursive algorithm
fn factorial_recursion(f: i64) -> i64 {
    // Return 1 if f is 0 otherwise we multiply the current f by
    // the result of our current function f-1
    return if f <= 0 { 1 } else { f * factorial_recursion(f-1) }
}
```

## Benchmarking
Rust is a systems programming language and therefore runs this code with exceptional speed.
The looping function completed in roughly **6-8 microseconds** to calculate the factorial 10,
and recursion completed in **0-1 microseconds** to calculate the same.
Rust has several optimisations which makes recursion faster in this scenario.

The benchmarking function used is provided below:
```rust
fn benchmark(f: fn(i64) -> i64, arg: String) -> (i64, Duration) {
    let now = Instant::now();
    let loop_result: i64 = f(arg.trim().parse::<i64>().unwrap());
    return (loop_result, now.elapsed());
}
```
