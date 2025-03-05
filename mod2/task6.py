def out():
    return input()

s = input("Введите строку из 0 и 1: ")

count_zero = 0
count_one = 0

for char in s:
    if char == '0':
        count_zero += 1
    elif char == '1':
        count_one += 1

if count_zero == count_one:
    print("yes")
    out()
else:
    print("no")
    out()