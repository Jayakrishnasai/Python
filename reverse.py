size = int(input("fEnter the Number: "))
arr = [int(input(f"Enter the Number {i + 1}: ")) for i in range(size)]
print(arr)
print("The reverse of the number is: ",arr[::-1],end="")