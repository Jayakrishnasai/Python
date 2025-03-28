def findPosition(k, n):
    a = 0
    b = 1
    i = 2
    while i != 0:
        c = a + b
        a = b
        b = c
        if b % k == 0:
            return n * i
        i += 1
    return -1
k = int(input("Enter the number: "))
n = int(input("Enter the number: "))
print(f"The Position of the {k}th multiple of {n} in the Fibonacci series is:", findPosition(k, n))