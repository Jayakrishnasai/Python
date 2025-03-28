n = int(input("Enter the Number: "))
a, b, sum = 0, 1, 0
for i in range(n):
    c = a + b
    a = b
    b = c
    sum += c
    print(f"The {i+1}th Fibonacci number is: {c}")
print(f"The sum of the first {n} Fibonacci numbers is: {sum}")