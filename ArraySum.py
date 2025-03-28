arr = [int(input(f"Enter the number {i+1}: ")) for i in range(5)]
sum = 0
for i in arr:
    sum += i
print(f"The sum of the array is:", sum)
print("\n")
print("Using Function")
def sumofarray(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum
n = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter the number {i+1}: ")) for i in range(n)]
print(f"the sum of array is: ",sumofarray(arr))
print("\n")
print("Using Enumerate List")
list = [int(input(f"Enter the number {i+1}: ")) for i in range(n)]
sum = 0
for i, j in enumerate(list):
    sum += j
print(f"The sum of the array is:", sum)
print("\n")
print("Using Numpy")
import numpy as np
arr = np.array([int(input(f"Enter the number {i+1}: ")) for i in range(n)])
sum = np.sum(arr)
print(f"The sum of the array is:", sum)
