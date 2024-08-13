import sys
input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])

rope = []
index = 1
for i in range(n):
    rope.append(int(data[index]))
    index += 1

# 로프들의 견딜 수 있는 중량을 오름차순으로 정렬
rope.sort()

# 최대 중량 계산
max_weight = 0
for i in range(n):
    # 현재 로프를 포함한 로프들로 들 수 있는 최대 중량 계산
    max_weight = max(max_weight, rope[i] * (n - i))

print(max_weight)