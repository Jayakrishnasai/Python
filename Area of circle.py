import math
radius = float(input("Enter the radiud of the circle: "))
Circumference = 2 * math.pi * radius
print(f"The circumference of the circle with radius {radius} is: {Circumference}")
area = math.pi* radius ** 2
print(f"The area of the circle with radius {radius} is: {area}")

# Another Method
print("\nAnother Method")
import math
area = math.pi * pow(radius, 2)
Circumference = 2 * math.pi * pow(radius, 1)
print(f"The circumference of the circle with radius {radius} is: {Circumference}")
print(f"The area of the circle with radius {radius} is: {area}")

# Another Method
print("\nAnother Method")
import numpy as np
area = np.pi * radius ** 2
Circumference = 2 * np.pi * radius
print(f"The circumference of the circle with radius {radius} is: {Circumference}")
print(f"The area of the circle with radius {radius} is: {area}")

# Another Method
print("\nAnother Method")
def calculate_area(radius):
    return math.pi * radius ** 2
def calcualte_circumference(radius):
    return 2 * math.pi * radius
area = calculate_area(radius)
Circumference = calcualte_circumference(radius)
print(f"The circumference of the circle with radius {radius} is: {Circumference}")
print(f"The area of the circle with radius {radius} is: {area}")