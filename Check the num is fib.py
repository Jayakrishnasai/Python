import math
def isPerfectSquare(num):
    s = int(math.sqrt(num))
    return s * s == num
def isFibonacci(num):
    return isPerfectSquare(5 * num * num + 4) or isPerfectSquare(5 * num * num - 4)
n = int(input("Enter a number: "))
for i in range (0, n):
    if (isFibonacci(i) == True):
        print(i, "is a fibonacci number")
    else:
        print(i, "is not a fibonacci number")