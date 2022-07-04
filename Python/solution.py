# Get the positive integer from the command line
n = int(input("Enter a positive integer: "))


# We define a total and multiply that total by x until x is 0
# We subtract x by 1 every loop
# We return the total at the end
def find_factorial_with_loop(x):
    total = 1
    while x > 0:
        total = total * x
        x = x - 1
    return total


# We define a total with the value one as a default argument
# We call the function from within but modify the arguments
# Total is multiplied by x, and x is subtracted by 1
# We check if x is 0 and if not we continue to call our own function
# We return the total once x is 0
def find_factorial_with_recursion(x, total=1):
    return total if x == 0 else find_factorial_with_recursion(x-1, total*x)


# Ensure n is a positive integer
if n < 0:
    print("You have not entered a positive integer.")
else:
    print(f"The factorial of {n} using loop is {find_factorial_with_loop(n)}")
    print(f"The factorial of {n} using recursion is {find_factorial_with_recursion(n)}")


