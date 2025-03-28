print("Using Formula")
n = int(input("Enter the number: "))
res = ((n * (n + 1)) // 2) ** 2
print(f"The sum of Cubes of first {n} numbers is:", res)

print("\n")
print("Using Brute Force")
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(f"The sum of Cubes of first {n} numbers is:", sum)
