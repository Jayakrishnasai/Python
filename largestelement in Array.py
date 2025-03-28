n = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter the number {i+1}: ")) for i in range(n)]
max = arr[0]
for i in range(1, n):
    if arr[i] > max:
        max = arr[i]
print(f"The largest element in the array is:", max)
print("\n")
print("Using Function")
def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
n = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter the number {i+1}: ")) for i in range(n)]
print(f"The largest element in the array is:", largest(arr))
print("\n")
print("Using Max Function")
max_v = max(arr)
print(f"The largest element in the array is:", max_v)
