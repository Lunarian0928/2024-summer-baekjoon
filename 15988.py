t = int(input()) # 테스트 케이스의 개수

# 테스트 케이스에서 입력한 수 중 가장 큰 수를
# dp 테이블의 사이즈를 할당하는데 사용하기 위함
max_size = 0 
# 입력했던 수들의 집합
arr = []

for _ in range(t):
    n = int(input()) # 입력한 정수
    arr.append(n)
    max_size = max(max_size, n)

max_size += 1 
if (max_size < 4):
    max_size = 4 

dp = [0 for _ in range(max_size)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

divisor = pow(10, 9) + 9 # 1,000,000,000 + 9

for i in range(4, max_size):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % divisor

for num in arr:
    print(dp[num])