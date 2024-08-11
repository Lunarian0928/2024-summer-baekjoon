n = int(input())
wine = []

wine.append(0)  
for _ in range(n):
    wine.append(int(input()))

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
elif n == 3:
    print(max(wine[1] + wine[2], wine[1] + wine[3], wine[2] + wine[3]))
else:
    dp = [0 for _ in range(n + 1)]
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    dp[3] = max(wine[1] + wine[2], wine[1] + wine[3], wine[2] + wine[3])

    for i in range(4, n + 1):
        dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i])

    print(max(dp))
