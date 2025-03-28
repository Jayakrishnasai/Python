n = int(input("Enter the number: "))
a = 0
b = 1
if n == 0:
    print("The 0th Fibonacci number is:",a, end = " ")
elif n == 1:
    print("The 1st Fibonacci number is:",b, end = " ")
else:
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print(f"\nthe {n}th Fibonacci number is:", a, end = " ")
# # Another way to find Fibonacci numbers
# print("\n")
def fibon(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibon(n-1) + fibon(n-2)
n = int(input("\nEnter the number: "))
print(f"The {n}th Fibonacci number is:", fibon(n))