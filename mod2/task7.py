def out():
    return input()

s, i = input("Введите строку и символ через запятую: ").split(',')

s = s.strip()
i = i.strip()

count = 0
for char in s:
    if char == i:
        count += 1
    else:
        break

print(count)
out()