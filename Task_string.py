s = input().strip()
for ch in s:
    if ord(ch) < 97:
        ch = chr(ord(ch) + 32)
    if ch not in ['a', 'y', 'o', 'e', 'u', 'i']:
        print(f".{ch}", end="")
print()
