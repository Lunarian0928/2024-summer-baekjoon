n = int(input())
flower = []
for _ in range(n):
    flowering_month, flowering_date, falling_month, falling_date = map(int, input().split())
    flowering_day = flowering_month * 100 + flowering_date
    falling_day = falling_month * 100 + falling_date
    flower.append([flowering_day, falling_day])

# 꽃이 피는 날을 기준으로 정렬, 같은 날 피는 꽃은 지는 날이 늦은 순서로 정렬
flower.sort()

current_end = 301  # 3월 1일을 나타냄
max_end = 301
count = 0
i = 0

while i < n and current_end <= 1130:
    flag = False
    while i < n and flower[i][0] <= current_end:
        if flower[i][1] > max_end:
            max_end = flower[i][1]
            flag = True
        i += 1
    
    if flag:  # 범위를 늘릴 수 있으면
        count += 1
        current_end = max_end
    else:  # 더 이상 범위를 늘릴 수 없으면
        break

# 마지막에 11월 30일 이후까지 커버했는지 확인
if current_end > 1130:
    print(count)
else:
    print(0)