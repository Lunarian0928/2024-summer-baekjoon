n = int(input())

stair = []
stair.append(0)

for _ in range(n):
    stair.append(int(input()))

if (n == 1):
    print(stair[1])
elif (n == 2):
    print(stair[1] + stair[2])
elif (n == 3):
    print(max(stair[2] + stair[3], stair[1] + stair[3]))
else:
    dp = [0 for _ in range(n + 1)]
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]
    dp[3] = max(stair[2] + stair[3], stair[1] + stair[3])
    
    for i in range(4, n + 1):
        dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])
        
    print(dp[n])