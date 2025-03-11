def check_numbers(numbers):
    unique = set(numbers)
    if len(unique) == 1:
        print("Все числа равны")
    elif len(unique) == len(numbers):
        print("Все числа разные")
    else:
        print("Есть равные и неравные числа")

check_numbers(list(map(int, input().split())))
input()