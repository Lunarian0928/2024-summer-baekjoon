cnts = [0] * 10
a = int(input())
b = int(input())
c = int(input())
multiplied = a * b * c
multiplied = str(multiplied)

for ch in multiplied:
    cnts[ord(ch) - ord('0')] += 1

for cnt in cnts:
    print(cnt)