t, w = map(int, input().split())

drop_it = []
for _ in range(t):
    drop_it.append(int(input()))

# dp 배열 초기화
dp = [[[0 for _ in range(2)] for _ in range(w + 1)] for _ in range(t)]

# 초기 조건 설정
if drop_it[0] == 1:
    dp[0][0][0] = 1
else:  # drop_it[0] == 2
    dp[0][1][1] = 1

for time in range(1, t):
    for move_cnt in range(w + 1):
        # 현재 1번 나무 아래에 있을 경우
        if drop_it[time] == 1:
            dp[time][move_cnt][0] = dp[time - 1][move_cnt][0] + 1
        else:
            dp[time][move_cnt][0] = dp[time - 1][move_cnt][0]
        
        # 현재 2번 나무 아래에 있을 경우
        if drop_it[time] == 2 and move_cnt > 0:
            dp[time][move_cnt][1] = dp[time - 1][move_cnt][1] + 1
        elif move_cnt > 0:
            dp[time][move_cnt][1] = dp[time - 1][move_cnt][1]

        if move_cnt > 0:
            dp[time][move_cnt][0] = max(dp[time][move_cnt][0], dp[time - 1][move_cnt - 1][1] + (1 if drop_it[time] == 1 else 0))
            dp[time][move_cnt][1] = max(dp[time][move_cnt][1], dp[time - 1][move_cnt - 1][0] + (1 if drop_it[time] == 2 else 0))

# 최대 자두 개수 계산
result = max(max(dp[t - 1][move_cnt][0], dp[t - 1][move_cnt][1]) for move_cnt in range(w + 1))
print(result)