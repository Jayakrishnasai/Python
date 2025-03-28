import math
def area_of_circle(radius):
    area = math.pi * pow(radius, 2)
    return area
def circumference_of_circle(radius):
    circumference = 2 * math.pi * radius
    return circumference
def area_of_square(side):
    area = pow(side, 2)
    return area
def perimeter_of_square(side):
    perimeter = 4 * side
    return perimeter
def area_of_rectangle(lenght, breadth):
    area = lenght * breadth
    return area
def perimeter_of_rectangle(lenght, breadth):
    perimeter = 2 * (lenght + breadth)
    return perimeter
def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area
def perimeter_of_triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter
def area_of_trapezium(base1, base2, height):
    area = 0.5 * (base1 + base2) * height
    return area
def perimeter_of_trapezium(base1, base2, side1, side2):
    perimeter = base1 + base2 + side1 + side2
    return perimeter
def area_of_parallelogram(base, height):
    area = base * height
    return area
def perimeter_of_parallelogram(base, side):
    perimeter = 2 * (base + side)
    return perimeter
def area_of_rhombus(diagonal1, diagonal2):
    area = 0.5 * diagonal1 * diagonal2
    return area
def perimeter_of_rhombus(side):
    perimeter = 4 * side
    return perimeter
radius = float(input("Enter the radius of the circle: "))
side = float(input("Enter the side of the square: "))
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))
base1 = float(input("Enter the first base of the trapezium: "))
base2 = float(input("Enter the second base of the trapezium: "))
diagonal1 = float(input("Enter the first diagonal of the rhombus: "))
diagonal2 = float(input("Enter the second diagonal of the rhombus: "))
side = float(input("Enter the side of the rhombus: "))
base = float(input("Enter the base of the parallelogram: "))
side = float(input("Enter the side of the parallelogram: "))
print(f"The area of the circle is: {area_of_circle(radius)}")
print(f"The circumference of the circle is: {circumference_of_circle(radius)}")
print(f"The area of the square is: {area_of_square(side)}")
print(f"The perimeter of the square is: {perimeter_of_square(side)}")
print(f"The area of the rectangle is: {area_of_rectangle(length, breadth)}")
print(f"The perimeter of the rectangle is: {perimeter_of_rectangle(length, breadth)}")
print(f"The area of the triangle is: {area_of_triangle(base, height)}")
print(f"The perimeter of the triangle is: {perimeter_of_triangle(side1, side2, side3)}")
print(f"The area of the trapezium is: {area_of_trapezium(base1, base2, height)}")
print(f"The perimeter of the trapezium is: {perimeter_of_trapezium(base1, base2, side1, side2)}")
print(f"The area of the parallelogram is: {area_of_parallelogram(base, height)}")
print(f"The perimeter of the parallelogram is: {perimeter_of_parallelogram(base, side)}")
print(f"The area of the rhombus is: {area_of_rhombus(diagonal1, diagonal2)}")
print(f"The perimeter of the rhombus is: {perimeter_of_rhombus(side)}")