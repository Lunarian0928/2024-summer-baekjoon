max_size = 1000
dp = [0 for _ in range(max_size + 1)]

dp[1] = 1 
# -
dp[2] = 2
# =, ||
dp[3] = 3
# |||, |=, =| 
dp[4] = 5
# ||||, ||=. |=|, =||, ==

for i in range(5, max_size + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
    
n = int(input())
print(dp[n] % 10007)