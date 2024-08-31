def check_cnt(mid):
    cnt = 1
    last_pos = arr[0]
    for i in range(1, len(arr)):
        gap = arr[i] - last_pos
        if (gap >= mid):
            cnt += 1
            last_pos = arr[i]
    return cnt

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1] - arr[0]

best_gap = 0
while (start <= end):
    mid = (start + end) // 2
    # 설치할 수 있는 공유기의 개수가 c개 이상일 경우
    # 설치 간격을 늘려, 공유기의 개수를 줄이도록 함
    if (check_cnt(mid) >= c): 
        best_gap = max(best_gap, mid)
        start = mid + 1
    # 설치할 수 있는 공유기의 개수가 c개 미만일 경우
    # 설치 간격을 줄여, 공유기의 개수를 늘리도록 함
    else:
        end = mid - 1
        
print(best_gap)