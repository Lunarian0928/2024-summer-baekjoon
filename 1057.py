n, a, b = map(int, input().split())

round = 0
while (a != b):
    a -= a // 2
    b -= b // 2
    print(f'a: {a}, b: {b}')
    round += 1

if (a == b):
    print(round)
else:
    print(-1)