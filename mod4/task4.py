def make_palindrome(s):
    from collections import Counter
    count = Counter(s)
    odd_chars = [char for char, cnt in count.items() if cnt % 2 != 0]
    if len(odd_chars) > 1:
        return "Нельзя составить палиндром"
    middle = odd_chars[0] if odd_chars else ""
    half = "".join([char * (cnt // 2) for char, cnt in count.items()])
    return half + middle + half[::-1]

s = input().strip()
print(make_palindrome(s))
input()