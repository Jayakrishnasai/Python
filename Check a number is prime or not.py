from sympy import*
amb = int(input("Enter the number1: "))
mba = int(input("Enter the number1: "))
if isprime(amb) == True and isprime(mba) == True:
    print("Both numbers are prime.")
elif isprime(amb) == False and isprime(mba) == False:
    print("Both numbers are not prime.")
elif isprime(amb) == True and isprime(mba) == False:
    print(f"{amb} is prime and {mba} is not prime.")
elif isprime(amb) == False and isprime(mba) == True:
    print(f"{amb} is not prime and {mba} is prime.")
else:
    print("Invalid Input")

# # Another way to check prime numbers
print("\n")
import math
n = int(input("Enter a number: "))
if n <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Prime" if is_prime else "Not" )

# Another way to check prime numbers
print("\n")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
