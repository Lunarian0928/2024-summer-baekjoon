# 회의 개수 입력
n = int(input().strip())
meetings = []

# 회의 정보 입력받기
for _ in range(n):
    start, end = map(int, input().strip().split())
    meetings.append((start, end))

# 종료 시간을 기준으로 정렬 (시작 시간이 같을 경우 종료 시간이 빠른 것 우선)
meetings.sort(key=lambda x: (x[1], x[0]))

# print(meetings)

# 회의 배정
count = 0
last_end_time = 0

for start, end in meetings:
    # print(f'last_end_time: {last_end_time}')
    # print(f'start: {start}, end: {end}')
    if start >= last_end_time:
        count += 1
        last_end_time = end

print(count)