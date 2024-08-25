import sys
from math import sqrt

input = sys.stdin.read

# 입력할 수 있는 숫자의 최대값
max_range = 10 ** 6
# 소수인지 여부
is_prime = [True] * (max_range + 1)
is_prime[0] = is_prime[1] = False
# 소수 리스트
primes = []

# 에라토스테네스의 체를 이용한 소수 생성
for i in range(2, max_range + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * 2, max_range + 1, i):
            is_prime[j] = False

data = input().split()
index = 0
t = int(data[index]) # 테스트 케이스의 수
index += 1

for _ in range(t):
    partition_cnt = 0  # 골드바흐 파티션의 수
    n = int(data[index])
    index += 1
    
    for i in primes:
        if i > n // 2: 
            break
        if is_prime[n - i]: 
            partition_cnt += 1
    
    print(partition_cnt)