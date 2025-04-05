a = [int(input(f"Enter the Number {i + 1}: ")) for i in range(int(input("Enter the size of the Array: ")))]
k = int(input("Enter the number of rotations you need: "))
c = a[-k:] + a[ :-k]
print(f"The rotated array is: {c}")