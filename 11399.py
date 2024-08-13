n = int(input())
taken_time = list(map(int, input().split()))
taken_time.sort()

total_time = 0
waiting_time = 0
for i in range(n):
    total_time += taken_time[i] + waiting_time
    waiting_time += taken_time[i]
print(total_time)