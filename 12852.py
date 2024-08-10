n = int(input())

# 첫번째 item: 연산 횟수 
# 두번째 item: 직전의 숫자
dp = [[0, 0] for _ in range(0, n + 1)]

dp[1][0], dp[1][1] = 0, 2

for i in range(2, n + 1):
    # 연산 3. 1을 뺀다
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = i - 1
    
    # 연산 2. x가 2로 나누어 떨어지면 2로 나눈다
    if (i % 2 == 0):
        if (dp[i][0] > dp[i // 2][0] + 1):
            dp[i][0] = dp[i // 2][0] + 1 
            dp[i][1] = i // 2
        
    # 연산 1. x가 3으로 나누어 떨어지면 3으로 나눈다
    if (i % 3 == 0):
        if (dp[i][0] > dp[i // 3][0] + 1):
            dp[i][0] = dp[i // 3][0] + 1
            dp[i][1] = i // 3
    
print(dp[n][0])


arr = []
cur = n
arr.append(cur)

while (cur != 1):
    cur = dp[cur][1]
    arr.append(cur)

for ans in arr:
    print(ans, end = ' ')