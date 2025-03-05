def out():
    return input()

input_data = input("Введите список слов через пробел: ")

words = []
current_word = ""
for char in input_data:
    if char == " ":
        if current_word:
            words.append(current_word)
            current_word = ""
    else:
        current_word += char
if current_word:
    words.append(current_word)

new_word = ""
for word in words:
    if word:
        new_word += word[-1]

print(new_word)
out()