def simple_interest(principal, rate, time):
    """Calculate simple interest."""
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))
interest = simple_interest(principal, rate, time)
print(f"The simple interest is: {interest}")


p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time (in years): "))
si = (p * r * t) / 100
print(f"The simple interest is: {si}")

def sim(principal, rate, time): # Imported Values from 1st Implemented Function
    return (principal * rate * time) / 100
print("Simple Interest Calculator")
print(f"Simple Interest: {sim(principal, rate, time)}")