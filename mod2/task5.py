def out():
    return input()

domain = input("Введите доменное имя: ")

parts = []
current_part = ""
for char in domain:
    if char == '.':
        if current_part:
            parts.append(current_part)
            current_part = ""
    else:
        current_part += char
if current_part:
    parts.append(current_part)

for i in range(len(parts) - 1, -1, -1):
    print(parts[i])
out()