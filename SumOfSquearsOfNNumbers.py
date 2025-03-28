m = int(input("Enter the number: "))
sum = 0
for i in range(1, m + 1):
    sum += i * i
print(f"The sum of squares of first {m} numbers is:", sum)
# # Another way to find the sum of squares of first n numbers
# print("\n")
def squaresum(n):
    return (n * (n + 1) * (2 * n + 1)) // 6
n = int(input("Enter the number: "))
print(f"The sum of squares of first {n} numbers is:", squaresum(n))

# # Another way to find the sum of squares of first n numbers
# print("\n")
def squaresum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum
n = int(input("Enter the number: "))
print(f"The sum of squares of first {n} numbers is:", squaresum(n))

# # Another way to find the sum of squares of first n numbers
# print("\n")
def squaresum(n):
    return (n * (n + 1) / 2) * (2 * n + 1) / 3
n = int(input("Enter the number: "))
print(f"The sum of squares of first {n} numbers is:", squaresum(n))