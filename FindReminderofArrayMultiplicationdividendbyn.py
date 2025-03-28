def findreminder(arr, n, d):
    mul = 1
    for i in range(n):
        mul = mul * arr[i]
    reminder = mul % d
    return reminder
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(int(input("Enter the number of elements in the array or Size of the Array: ")))]
n = len(arr)
d = int(input("Enter the divisor: "))
print("The Reminder of Array multiplication divisor is : ", findreminder(arr, n, d))
