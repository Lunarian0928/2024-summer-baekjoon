n = int(input())
max_size = pow(10, 6) + 1
dp = [0 for _ in range(max_size)]

dp[1] = 1
# 1
dp[2] = 2
# 00, 11
dp[3] = 3
# 100, 001, 111
dp[4] = 5
# 0000, 1001, 0011, 1100, 1111

for i in range(5, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 15746
    
print(dp[n])