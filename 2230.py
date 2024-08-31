n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))
arr.sort()

start = 0
end = 1

best_gap = float('inf')
while (start <= end) and (start <= n - 1) and (end <= n - 1):
    gap = abs(arr[end] - arr[start])
    if (gap == m):
        best_gap = m
        break
    # gap을 줄이는 방향으로 탐색해야 되기 때문에
    # start를 뒤로 이동
    elif (gap > m):
        best_gap = min(best_gap, gap)
        start += 1
    # gap을 늘리는 방향으로 탐색해야 되기 때문에
    # end를 뒤로 이동
    else:
        end += 1
print(best_gap)