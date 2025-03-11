def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# Пример использования
a, b = map(int, input().split())
print(gcd(a, b))