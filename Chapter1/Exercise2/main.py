PI = 3.14

height = float(input("Height of Cylinder: "))
radius = float(input("Radius of Cylinder: "))

volume = height * (radius ** 2) * PI
surArea = (2 * PI * radius * height) + (2 * PI * (radius ** 2))

print("Volume of Cylinder: ", volume)
print("Surface Area of Cylinder: ", surArea)