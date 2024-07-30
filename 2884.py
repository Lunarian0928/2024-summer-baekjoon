h, m = map(int, input().split())

time = h * 60 + m - 45

h = time // 60
h %= 24

m = time % 60
m %= 60

print(h, m)