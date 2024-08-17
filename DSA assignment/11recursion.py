def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate the factorial of a number
result = factorial(int(input("Enter the value:")))
print(f"The factorial of  given number  is: {result}")


#tail recursion
def factorial_tail_recursive(n, result=1):
    if n == 0:
        return result
    else:
        return factorial_tail_recursive(n - 1, n * result)

# Calculate the factorial of a number using tail recursion
result = factorial_tail_recursive(6)
print(f"The factorial of 6 is {result}")

#non tail recursion
def factorial_non_tail_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_non_tail_recursive(n - 1)

# Calculate the factorial of a number using non-tail recursion
result = factorial_non_tail_recursive(5)
print(f"The factorial of 5 is {result}")
