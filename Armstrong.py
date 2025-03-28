def armstrong(num):
    sum = 0
    temp = num
    while temp != 0:
        r = temp % 10
        sum += r ** len(str(num))
        temp //= 10
    if sum == num:
        print(f"{num} is an Armstrong Number")
    else:
        print(f"{num} is not an Armstrong Number")

number = int(input("Enter the number: "))
armstrong(number)

n = int(input("Enter a number: "))
if n < 0:
    print(f"{n} is not a valid number.")
elif n == 0:
    print(f"{n} is an Armstrong number.")
else:
    sum = 0
    temp = n
    s = len(str(n))
    while temp != 0:
        r = temp % 10
        sum += r ** s
        temp //= 10
    if sum == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")
