# def findremonder(arr, len, n):
#     mul = 1
#     for i in range(n):
#         mul = (mul * (arr[i] % n)) % n
#     return mul % n

# arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(int(input("Enter the number of elements in the array or Size of the Array: ")))]
# len = len(arr)
# n = int(input("Enter the divisor: "))
# print("The Reminder of Array multiplication divisor is : ", findremonder(arr, len, n))

# # The Reminder of Array multiplication divisor is :  0
def finreminder(arr, len, n):
    mul = 1
    for i in range(len):
        mul *= arr[i]
    return mul % n
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(int(input("Enter the number of elements in the array or Size of the Array: ")))]
len = len(arr)
n = int(input("Enter the divisor: "))
print("The Reminder of Array multiplication divisor is : ", finreminder(arr, len, n))