a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# if a > b:
#     print("Invalid Range")
# else:
#     for i in range(a, b + 1): # 0 to 51
#         is_prime = True
#         if i < 2:    # 0 and 1 are not prime numbers, So we skip them
#             continue
#         for j in range(2, i):  # E.g.. 2 to 50
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(i, end=" ")

if a > b:
    print("negative Number are Invalid Numbers. ")
else:
    for i in range(a, b + 1):
        is_prime = True
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")  

# Another way to check prime numbers
print("\n")
from sympy import primerange
x = int(input("Enter the number of prime numbers you want: "))
y = int(input("Enter the number of prime numbers you want: "))
primes = list(primerange(x, y + 1))
print("The prime numbers in the range are: ", primes if primes else "No prime numbers found.")
