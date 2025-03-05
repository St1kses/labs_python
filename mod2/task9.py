def out():
    return input()

phone_number = input("Введите номер телефона: ")

# Очистка номера от лишних символов
cleaned_number = ""
for char in phone_number:
    if char in "+0123456789":  # Оставляем только цифры и плюс
        cleaned_number += char

print(cleaned_number)
out()