import math
# a: 낮에 올라갈 수 있는 길이(m)
# b: 밤에 자는 동안 미끄러지는 길이(m)
# v: 나무 막대의 길이(m)
a, b, v = map(int, input().split())

day = math.ceil((v - b)/(a - b))
print(day)