n = int(input())
p = list(map(int, input().split()))

dp = [0] * (n + 1)

# ex)
# n = 4
# p [1, 5, 6, 7]
for i in range(1, n + 1):
    for j in range(1, i + 1):
        # ex) i = 2, j = 1
        # dp[2], dp[1] + p[0] = 1 + 1 = 2
        # ex) i = 2, j = 2
        # dp[2], dp[0] + p[2] = 0 + 5 = 5
        dp[i] = max(dp[i], dp[i - j] + p[j - 1])
print(dp[n])