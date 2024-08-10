# 입력받는 정수 n의 최댓값
max_size = 40
# 첫번째 아이템: 0이 출력되는 횟수
# 두번째 아이템: 1이 출력되는 횟수
dp = [[-1, -1] for _ in range(max_size + 1)]

dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1

# 피보나치 수의 정의에 따름
for i in range(2, max_size + 1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

t = int(input())
arr = []
for _ in range(t):
    n = int(input())
    arr.append(n)

for n in arr:
    print(dp[n][0], dp[n][1])