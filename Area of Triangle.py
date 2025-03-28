base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

# Another method using the math module
print("\nAnother Method")
def area_of_Triangle(base, height):
    return 0.5 * base * height
print(f"area of Triangle is: {area_of_Triangle(base, height)}")

