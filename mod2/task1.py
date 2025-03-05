
input_data = str(input("Введите числа a и b через запятую: "))

numbers = input_data.split(',')

a = int(numbers[0].strip())
b = int(numbers[1].strip())

remainder = a % b

print(remainder)
input()