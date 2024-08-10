# 집의 수
n = int(input())  

# 각 집을 빨강, 초록, 파랑으로 칠하는 비용
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

# 이전의 집을 고려하여, i번째 집을 칠할 때의 코스트
dp = [[0 for _ in range(3)] for _ in range(n)]

dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, n):
    dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = cost[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = cost[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n - 1]))