import math


def square(side):
    area = side * side
    return math.ceil(area)


side_length = 5.7
result = square(side_length)

print("Площадь квадрата со стороной", side_length, "равна:", result)
