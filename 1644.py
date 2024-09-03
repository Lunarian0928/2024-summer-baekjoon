n = int(input())
# 소수인지 여부가 저장된 리스트
is_prime = [True for _ in range(n + 1)]
# 0과 1은 소수에서 제외
is_prime[0] = is_prime[1] = False
# 소수 목록
primes = []

# 에라토스테네스의 체로
# is_prime과 primes를 업데이트
for i in range(2, n + 1):
    if (is_prime[i]):
        primes.append(i)
        for j in range(i + i, n + 1, i):
            is_prime[j] = False
            
start = 0 
total = 0 # 연속된 소수의 합
cnt = 0 # 연속된 소수의 합으로 표현할 수 있는 경우의 수
for end in range(0, len(primes)):
    total += primes[end] # 슬라이딩 윈도우를 확장
    while (total >= n):
        if (total == n): # 연속된 소수의 합으로 n을 표현할 수 있는 경우
            cnt += 1 # 경우의 수를 카운트
        total -= primes[start]
        start += 1 # 슬라이딩 윈도우를 축소
    
print(cnt) # 정답 출력