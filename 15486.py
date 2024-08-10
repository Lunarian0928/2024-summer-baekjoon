import sys
input = sys.stdin.read

data = input().split()
index = 0
n = int(data[index])

schedule = []
index = 1

for _ in range(n):
    taken_day, pay = int(data[index]), int(data[index + 1])
    schedule.append([taken_day, pay])
    index += 2

dp = [0] * (n + 1)

for day in range(n):
    taken_day, pay = schedule[day][0], schedule[day][1]
    payday = day + taken_day

    # 현재 상담을 하지 않았을 때 다음 날까지의 최대 수익을 갱신
    if day + 1 <= n:
        dp[day + 1] = max(dp[day + 1], dp[day])

    # 상담이 끝나는 날에 대한 최대 수익을 갱신
    if payday <= n:
        dp[payday] = max(dp[payday], dp[day] + pay)
    
print(max(dp))