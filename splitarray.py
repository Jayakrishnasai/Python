def splitArr(arr, n, k):
    # n = Size of the array
    # k = Number of elements to be split
    # arr = Array to be split
    arr1 = arr[:k]
    arr2 = arr[k:n]
    return arr1, arr2
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(int(input("Enter the number of elements in the array or Size of the Array: ")))]
k = int(input("Enter the number of elements to be split: "))
arr1, arr2 = splitArr(arr, len(arr), k)
print(f"The first part of the array is: {arr1}")
print(f"The second part of the array is: {arr2}")