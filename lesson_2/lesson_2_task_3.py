import math
def square():
      side = float(input('Если сторона квадрата = '))
      side_square=math.ceil(side)
      area = side_square * side_square
      if isinstance(side, int) or isinstance(side, float):
          return area
print("То площадь квадрата = ", square())