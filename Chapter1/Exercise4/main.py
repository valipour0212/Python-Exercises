from math import tan, pi

nSides = int(input('Enter number of sides: '))
sLength = float(input('Enter the length of the sides: '))

pArea = nSides * (sLength ** 2) / (4 * tan(pi / sLength))

print('The area of the polygon is', pArea)
