def out():
    return input()

input_data = input("Введите три числа через пробел: ")

numbers = []
current_number = ""
for char in input_data:
    if char == " ":
        if current_number:
            num = int(current_number)
            if not (-1000 <= num <= 1000):
                print("Ошибка: числа должны быть в диапазоне от -1000 до 1000.")
                out()
                exit()
            numbers.append(num)
            current_number = ""
    else:
        current_number += char
if current_number:
    num = int(current_number)
    if not (-1000 <= num <= 1000):
        print("Ошибка: числа должны быть в диапазоне от -1000 до 1000.")
        out()
        exit()
    numbers.append(num)

a, b, c = numbers
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print(b)
out()