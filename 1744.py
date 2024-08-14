n = int(input())

pos = []
neg = []
zero_cnt = 0
one_cnt = 0

for _ in range(n):
    num = int(input())
    if num == 0:
        zero_cnt += 1
    elif num == 1:
        one_cnt += 1
    elif num > 0:
        pos.append(num)
    else:
        neg.append(num)

# 양수는 내림차순, 음수는 오름차순 정렬
pos.sort(reverse=True)
neg.sort()

ans = 0

# 양수 리스트 처리
while len(pos) > 1:
    ans += pos.pop(0) * pos.pop(0)

# 양수 하나가 남아있으면 더해준다.
if len(pos) == 1:
    ans += pos.pop()

# 음수 리스트 처리
while len(neg) > 1:
    ans += neg.pop(0) * neg.pop(0)

# 음수 하나가 남아있고 0이 없다면 남은 음수를 더해준다.
if len(neg) == 1:
    if zero_cnt == 0:
        ans += neg.pop()

# 1의 개수를 더해준다.
ans += one_cnt

print(ans)