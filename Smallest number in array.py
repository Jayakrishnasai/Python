n = int(input("Enter the number of elements in array: "))
arr = [int(input(f"Enter the number {i+1}: ")) for i in range(n)]
min = arr[0]
for i in range(1, n):
    if arr[i] < min:
        min = arr[i]
print(f"The smallest element in the array is:", min)