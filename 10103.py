n = int(input())

# s1: 창영이의 점수
# s2: 상덕이의 점수
s1, s2 = 100, 100
for i in range(0, n):
    # d1, d2: 두 사람의 주사위 수
    d1, d2 = map(int, input().split())
    if (d1 > d2):
        s2 -= d1
    elif (d1 < d2):
        s1 -= d2

print(s1) 
print(s2)