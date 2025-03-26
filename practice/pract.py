def number_to_word(n, gender="male"):
    numbers = {
        "male": ["ноль", "один", "два", "три", "четыре",
                 "пять", "шесть", "семь", "восемь", "девять"],
        "female": ["ноль", "одна", "две", "три", "четыре",
                   "пять", "шесть", "семь", "восемь", "девять"]
    }
    return numbers[gender][n]


def date_to_word(n):
    if n < 1 or n > 31:
        return ""

    if 11 <= n <= 19:
        teens = ["одиннадцатое", "двенадцатое", "тринадцатое",
                 "четырнадцатое", "пятнадцатое", "шестнадцатое",
                 "семнадцатое", "восемнадцатое", "девятнадцатое"]
        return teens[n - 11]

    tens = n // 10
    units = n % 10

    tens_words = ["", "десятое", "двадцатое", "тридцатое"]
    units_words = [
        "", "первое", "второе", "третье", "четвертое",
        "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое"
    ]

    if tens == 0:
        return units_words[units]
    elif tens == 1:
        return "десятое"
    elif tens == 2:
        return "двадцатое" if units == 0 else f"двадцать {units_words[units]}"
    elif tens == 3:
        return "тридцатое" if units == 0 else f"тридцать {units_words[units]}"
    return ""


def month_to_word(n):
    months = [
        "января", "февраля", "марта", "апреля",
        "мая", "июня", "июля", "августа",
        "сентября", "октября", "ноября", "декабря"
    ]
    return months[n - 1] if 1 <= n <= 12 else ""


def year_to_word(n):
    if n < 0 or n > 9999:
        return ""

    if n == 0:
        return "нулевого"

    if n % 1000 == 0:
        thousands = n // 1000
        if thousands == 1:
            return "тысячного"
        elif thousands == 2:
            return "двухтысячного"
        else:
            word = number_to_word(thousands, "female")
            if word == "три":
                word = "трёх"
            elif word.endswith('ь'):
                word = word[:-1] + 'и'
            return f"{word}тысячного"

    if n < 1000:
        parts = []
        hundreds = n // 100
        remainder = n % 100

        if hundreds > 0:
            if hundreds == 1:
                parts.append("сто")
            elif hundreds == 2:
                parts.append("двести")
            elif hundreds == 3:
                parts.append("триста")
            elif hundreds == 4:
                parts.append("четыреста")
            elif hundreds >= 5:
                word = number_to_word(hundreds)
                if word == "три":
                    word = "трёх"
                parts.append(f"{word}сот")

        if remainder > 0:
            if 10 <= remainder <= 19:
                teens = ["десять", "одиннадцать", "двенадцать", "тринадцать",
                         "четырнадцать", "пятнадцать", "шестнадцать",
                         "семнадцать", "восемнадцать", "девятнадцать"]
                parts.append(teens[remainder - 10])
            else:
                tens = remainder // 10
                units = remainder % 10

                if tens >= 2:
                    tens_words = ["двадцать", "тридцать", "сорок", "пятьдесят",
                                  "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
                    parts.append(tens_words[tens - 2])

                if units > 0:
                    parts.append(number_to_word(units, "male"))

        if parts:
            last_word = parts[-1]
            if last_word == 'один':
                parts[-1] = 'первого'
            elif last_word == 'два':
                parts[-1] = 'второго'
            elif last_word == 'три':
                parts[-1] = 'третьего'
            elif last_word == 'четыре':
                parts[-1] = 'четвертого'
            elif last_word == 'пять':
                parts[-1] = 'пятого'
            elif last_word == 'шесть':
                parts[-1] = 'шестого'
            elif last_word == 'семь':
                parts[-1] = 'седьмого'
            elif last_word == 'восемь':
                parts[-1] = 'восьмого'
            elif last_word == 'девять':
                parts[-1] = 'девятого'
            elif last_word.endswith('ть'):
                parts[-1] = last_word[:-2] + 'того'
            elif last_word.endswith('ь') or last_word.endswith('й'):
                parts[-1] = last_word[:-1] + 'ого'
            else:
                parts[-1] += 'ого'

        return ' '.join(parts)

    thousands = n // 1000
    remainder = n % 1000

    parts = []

    if thousands == 1:
        parts.append("одна тысяча")
    elif thousands == 2:
        parts.append("две тысячи")
    elif 3 <= thousands <= 4:
        word = number_to_word(thousands, "female")
        parts.append(f"{word} тысячи")
    elif thousands >= 5:
        word = number_to_word(thousands, "female")
        if word == "три":
            word = "трёх"
        parts.append(f"{word} тысяч")

    if remainder > 0:
        hundreds = remainder // 100
        tens_units = remainder % 100

        if hundreds == 1:
            parts.append("сто")
        elif hundreds == 2:
            parts.append("двести")
        elif hundreds == 3:
            parts.append("триста")
        elif hundreds == 4:
            parts.append("четыреста")
        elif hundreds >= 5:
            word = number_to_word(hundreds)
            if word == "три":
                word = "трёх"
            parts.append(f"{word}сот")

        if 10 <= tens_units <= 19:
            teens = ["десять", "одиннадцать", "двенадцать", "тринадцать",
                     "четырнадцать", "пятнадцать", "шестнадцать",
                     "семнадцать", "восемнадцать", "девятнадцать"]
            parts.append(teens[tens_units - 10])
        else:
            tens = tens_units // 10
            units = tens_units % 10

            if tens >= 2:
                tens_words = ["двадцать", "тридцать", "сорок", "пятьдесят",
                              "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
                parts.append(tens_words[tens - 2])

            if units > 0:
                parts.append(number_to_word(units, "male"))

    if parts:
        last_word = parts[-1]
        if last_word == 'один':
            parts[-1] = 'первого'
        elif last_word == 'два':
            parts[-1] = 'второго'
        elif last_word == 'три':
            parts[-1] = 'третьего'
        elif last_word == 'четыре':
            parts[-1] = 'четвертого'
        elif last_word == 'пять':
            parts[-1] = 'пятого'
        elif last_word == 'шесть':
            parts[-1] = 'шестого'
        elif last_word == 'семь':
            parts[-1] = 'седьмого'
        elif last_word == 'восемь':
            parts[-1] = 'восьмого'
        elif last_word == 'девять':
            parts[-1] = 'девятого'
        elif last_word.endswith('ть'):
            parts[-1] = last_word[:-2] + 'того'
        elif last_word.endswith('ь') or last_word.endswith('й'):
            parts[-1] = last_word[:-1] + 'ого'
        else:
            parts[-1] += 'ого'

    return ' '.join(parts)

date_str = input("Введите дату в формате DD.MM.YYYY: ")

try:
    day, month, year = map(int, date_str.split('.'))
except:
    print("Ошибка: неверный формат даты. Используйте DD.MM.YYYY")
    exit()

if not (1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 9999):
    print("Ошибка: введена некорректная дата")
    exit()

day_word = date_to_word(day)
month_word = month_to_word(month)
year_word = year_to_word(year)

print(f"{day_word} {month_word} {year_word} года")