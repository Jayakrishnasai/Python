def ismonotonic(arr):
    Inc = Dec = True
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            Dec = False
        elif arr[i] < arr[i - 1]:
            Inc = False
    return Inc or Dec
if ismonotonic == True:
    print("The array is monotonic")
else:
    print("The array is not monotonic")
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(int(input("Enter the number of elements in the array or Size of the Array: ")))]
n = len(arr)
print("The array is: ", arr)
if arr:
    if ismonotonic(arr):
        print("The array is monotonic")
    else:
        print("The array is not monotonic")
else:
    print("The array is empty")