m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
if m > n:
    print("Invalid Range")
else:
    sum = 0
    for i in range(m, n + 1):
        sum += i
    print(f"The sum of the numbers between {m} and {n} is: {sum}")
    
