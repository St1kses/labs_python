def out():
    return input()

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

def decimal_to_octal(n):
    if n == 0:
        return "0"
    octal = ""
    while n > 0:
        octal = str(n % 8) + octal
        n = n // 8
    return octal

def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        remainder = n % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        n = n // 16
    return hexadecimal

input_data = input("Введите натуральное число: ")

if not input_data.isdigit() or int(input_data) <= 0:
    print("Неверный ввод")
    out()
else:
    n = int(input_data)

    binary = decimal_to_binary(n)
    octal = decimal_to_octal(n)
    hexadecimal = decimal_to_hexadecimal(n)

    print(f"{binary}, {octal}, {hexadecimal}")
    out()