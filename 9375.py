import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()
index = 0

t = int(data[index]) # 테스트 케이스의 수
index += 1

result = [] # 정답을 담는 리스트
for _ in range(t):
		# key: 옷 종류, value: 개수
    closet = defaultdict(int)
    
    n = int(data[index])
    index += 1
    
    for _ in range(n):
        clothes, cloth_type = data[index], data[index + 1]
        index += 2
        closet[cloth_type] += 1
    
    # 의상을 입을 수 있는 경우의 수
    # 주어진 옷의 개수 + 옷을 안 입는 경우
    case_cnt = 1
    for num in closet.values():
        case_cnt *= (num + 1)
        
		# 옷을 아예 안 입는 경우는 제외하여야 함
    case_cnt -= 1
    result.append(case_cnt)
    
print("\n".join(map(str, result)))