a, b = map(int, input().split())
c = int(input())

# 계산하기 편하도록 분 단위로 시간을 계산
time = a * 60 + b + c 

# 1시간 = 60분
a = time // 60 % 24
b = time % 60

print(a, b)