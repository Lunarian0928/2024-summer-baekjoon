# n: 현재 휴게소의 개수
# m: 더 지으려고 하는 휴게소의 개수
# l: 고속도로의 길이
n, m, l = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

arr = [0] + arr + [l]

# 지을 수 있는 휴게소의 개수가 몇 개인지 확인
def check_cnt(mid): 
    cnt = 0
    for i in range(len(arr) - 1):
        gap = arr[i + 1] - arr[i]
        if (gap > mid):
            cnt += (gap - 1) // mid
    return cnt <= m 

start = 1
end = l

while (start <= end):
    mid = (start + end) // 2
    
    # 휴게소의 개수가 m개보다 작거나 같을 경우
    if (check_cnt(mid)):
        # 휴게소의 설치할 수 있는 간격을 줄이는 방향으로 탐색한다.
        end = mid - 1
    else:
        # 휴게소를 설치할 수 있는 간격을 늘리는 방향으로 탐색한다.
        start = mid + 1

# 구간의 최댓값의 최솟값
print(start)