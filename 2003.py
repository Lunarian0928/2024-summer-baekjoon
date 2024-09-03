# n: 수열의 개수
# m: 연속된 수열의 합으로 만들어야 하는 수
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
total = 0
cnt = 0
for end in range(len(arr)):
    total += arr[end]
    while (total >= m):
        if (total == m):
            cnt += 1
        total -= arr[start]
        start += 1

print(cnt)