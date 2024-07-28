import math

def square(side):
    side_square = math.ceil(side)
    return side_square * side_square

side = float(input('Если сторона квадрата = '))
print("То площадь квадрата = ", square(side))