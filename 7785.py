import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split('\n')
index = 0

# 로그에 기록된 출입 기록의 수
n = int(data[index].strip())
index += 1

# 로그
logs = [line.split() for line in data[index:index+n]]

# 사원이 회사에 남아있는지/퇴근했는지 저장하는 정보
dictionary = defaultdict()

# key를 이름 value를 record로 하여 dictionary에 저장
for name, record in logs:
    dictionary[name] = record
    
# 딕셔너리의 아이템을 키를 기준으로 정렬
sorted_items = sorted(dictionary.items(), reverse=True)

# 만약 마지막 기록이 enter라면 남아있다는 것으로
# 그 사원의 이름을 출력
for name, record in sorted_items:
    if record == 'enter':
        print(name)