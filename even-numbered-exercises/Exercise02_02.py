# Enter radius of the cylinder
radius = float(input("Enter the radius of a cylinder: "))
length = float(input("Enter the length of a cylinder: "))

area = radius * radius * 3.14159
volume = area * length

print("The area is", area)
print("The volume of the cylinder is", volume)