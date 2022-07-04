import time


def benchmark(function, *args, **kwargs):
    start = time.time_ns()
    f = function(*args, **kwargs)
    end = time.time_ns()
    print(f"Benchmarked {function.__name__} at {(end - start)} nanoseconds")
    return f


def find_factorial_with_loop(x):
    total = 1
    while x > 0:
        total = total * x
        x = x - 1
    return total


def find_factorial_with_recursion(x, total=1):
    return total if x == 0 else find_factorial_with_recursion(x-1, total*x)


if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    if n < 0:
        print("You have not entered a positive integer.")
    else:
        print(f"The factorial of {n} using loop is {benchmark(lambda: find_factorial_with_loop(n))}!")
        print(f"The factorial of {n} using recursion is {benchmark(lambda: find_factorial_with_recursion(n))}!")


