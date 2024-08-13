n = int(input())

max_size = n + 1
if (n <= 4):
    max_size = 5

dp = [False for _ in range(max_size)]
dp[1] = True
dp[2] = False
dp[3] = True
dp[4] = True

for i in range(5, max_size):
    dp[i] = not dp[i-1] or not dp[i-3] or not dp[i-4]

if (dp[n]):
    print("SK")
else:
    print("CY")