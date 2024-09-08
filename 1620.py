import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()
index = 0

n, m = int(data[index]), int(data[index + 1])
index += 2
num_to_name = defaultdict(str)
name_to_num = defaultdict(int)

for num in range(1, n+1):
    name = data[index].strip() # 입력받은 이름의 공백을 제거
    index += 1
    num_to_name[num] = name # 숫자 -> 이름 매핑
    name_to_num[name] = num # 이름 -> 숫자 매핑

# 쿼리 처리
result = []
for _ in range(m):
    query = data[index].strip() # 입력받은 쿼리의 공백을 제거
    index += 1
    if query.isdigit(): # 쿼리가 숫자인 경우
        result.append(num_to_name[int(query)]) # 숫자를 이용해 이름 출력
    else: # 쿼리가 이름인 경우
        result.append(name_to_num[query]) # 이름을 이용해 숫자 출력

# 결과 출력
print("\n".join(map(str, result)))