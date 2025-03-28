def splitArr(arr, n, k):
    k = k % n # To handle the case when k > n
    for i in range(k):
        x = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = x
    return arr
n = int(input("Enter the number of elements in the array or Size of the Array: "))
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(n)]
k = int(input("Enter the number of elements to be split: "))
arr = splitArr(arr, len(arr), k)
for i in range(n):
    print(f"The {i + 1}th element of the array is: {arr[i]}")
