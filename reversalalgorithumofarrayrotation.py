def reverseArray(arr, d):
    c = (arr[d:] + arr[:d])
    return c
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(int(input("Enter the number of elements in the array or Size of the Array: ")))]
d = int(input("Enter the number of rotations: "))
arr = reverseArray(arr, d)
print(f"The reversed array is: {arr}")

# using deque
from collections import deque
def reverseArray(arr, d):
    c = deque(arr)
    c.rotate(-d)
    return list(c)
arr = [int(input(f"Enter the number {i + 1}: ")) for i in range(int(input("Enter the number of elements in the array or Size of the Array: ")))]
d = int(input("Enter the number of rotations: "))
arr = reverseArray(arr, d)
print(f"The reversed array is: {arr}")