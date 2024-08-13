# 벽의 가로 길이
n = int(input())
if (n <= 4):
    if (n == 1):
        print(0)
    elif (n == 2):
        print(3)
    elif (n == 3):
        print(0)
    else:
        print(11)
    exit()
    
dp = [0 for _ in range(n + 1)]

dp[2] = 3
dp[4] = 11 

for i in range(6, n + 1, 2):
    dp[i] = dp[i-2] * 4 - dp[i-4]

print(dp[-1])