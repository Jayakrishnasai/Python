def rotateArray(arr, n, d):
    # n = Size of the array
    # d = Number of rotations
    # arr = Array to be rotated
    arr[:] = arr[d:n]+arr[0:d]
    return arr
n = int(input("Enter the number of elements in the array or Size of the Array: "))
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(n)]
d = int(input("Enter the number of rotations: "))
arr = rotateArray(arr, n, d)
print(f"The rotated array is: {arr}")
