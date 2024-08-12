n = int(input())

dp = [float('inf') for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1
# 1^2 = 1
# dp[2] = 2
# 1^2 + 1^2 = 2
# dp[3] = 3
# 1^2 + 1^2 + 1^2 = 3
# dp[4]=  1
# 2^2 = 4
# dp[5] = 2
# 2^2 + 1^2 = 5

for i in range(1, n + 1):
    j = 1
    while j * j <= i:
        dp[i] = min(dp[i], dp[i - j * j] + 1)    
        j += 1
    
print(dp[n])