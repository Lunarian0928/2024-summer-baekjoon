max_size = 1000

dp = [0 for _ in range(max_size + 1)]
dp[1] = 1
# -
dp[2] = 3
# =, ||, ㅁ
dp[3] = 5
# |||, =|, |=, ㅁ|, |ㅁ
dp[4] = 11
# ||||, ||=, |=|, =||, ||ㅁ, |ㅁ|, ㅁ||, ==, ㅁ=, =ㅁ, ㅁㅁ
for i in range(5, max_size + 1):
    dp[i] = dp[i - 2] * 2 + dp[i - 1]

n = int(input())
print(dp[n] % 10007)