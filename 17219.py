import sys
from collections import defaultdict
input = sys.stdin.read

data = input().split()
index = 0

# n: 저장된 사이트 주소의 수
# m: 비밀번호를 찾으려는 사이트 주소의 수
n, m = int(data[index]), int(data[index + 1])
index += 2

passwords = defaultdict(str)

# key는 사이트 주소, value는 비밀번호로 설정
for _ in range(n):
    site, password = data[index], data[index + 1]
    index += 2
    passwords[site] = password

for _ in range(m):
    site = data[index]
    index += 1
    print(passwords[site])