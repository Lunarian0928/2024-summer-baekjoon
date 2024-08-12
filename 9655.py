n = int(input()) # 돌의 개수

max_size = 1000
dp = [0 for _ in range(max_size + 1)]

dp[0] = 1
dp[1] = 1
# 1개 가져가기
dp[2] = 2
# 1개 가져가고, 1개 가져가기
dp[3] = 1
# 3개 가져가기

for i in range(4, max_size + 1):
    dp[i] += min(dp[i-1], dp[i-3]) + 1

if (dp[n] % 2 == 1):
    print("SK")
else:
    print("CY")
