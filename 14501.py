n = int(input())

arr = []
for start_day in range(1, n + 1):
    taken_day, wages = map(int, input().split())
    arr.append([taken_day, wages])
   
   
dp = [0 for _ in range(n+1)]

for day in range(0, n):
    for i in range(day + arr[day][0], n + 1):
        if (dp[i] < dp[day] + arr[day][1]):
            dp[i] = dp[day] + arr[day][1]

print(dp[-1])