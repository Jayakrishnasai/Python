def factorial(n):
    if n < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")

n = int(input("Enter a number to calculate its factorial: "))
if n < 0:
    print("Error: Factorial is not defines for negative numbers.")
elif n == 0 or  n == 1:
    print("The factorial of 0 or 1 is 1.")
else:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(f"The factorial of {n} is: {fact}")

def factorial(a):
    if a < 0:
        print("Error: Factorial is not defined for negative numbers.")
    elif a == 0 or a == 1:
        return 1
    else:
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result
number = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {number} is: {factorial(number)}")