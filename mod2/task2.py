import math

side_length = float(input("Введите длину стороны квадрата: "))

perimeter = 4 * side_length

area = side_length ** 2

diagonal = side_length * math.sqrt(2)

perimeter_rounded = round(perimeter, 2)
area_rounded = round(area, 2)
diagonal_rounded = round(diagonal, 2)

print(f"{perimeter_rounded}, {area_rounded}, {diagonal_rounded}")
input()