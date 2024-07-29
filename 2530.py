a, b, c = map(int, input().split())
d = int(input())

time = a * 60 * 60 + b * 60 + c + d

a = time // (60 * 60)
a %= 24

b = time // 60 % 60
b %= 60

c = time % 60
c %= 60

print(a, b, c)