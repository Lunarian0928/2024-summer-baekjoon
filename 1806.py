# n: 원소의 개수, s: 부분합의 합이 s 이상이어야 함
n, s = map(int, input().split())

# 수열
arr = list(map(int, input().split()))

start = 0
total = 0
# 부분합의 최소 길이
min_length = float('inf')

# 누적합 이용
for end in range(0, n):
    total += arr[end]
    
    while total >= s:    
        min_length = min(min_length, end - start + 1)
        total -= arr[start]
        start += 1

# 비록 total은 s 이상의 수가 아닐 수도 있으나
# min_length는 total >= s인 경우에만 업데이트하였으므로
# 문제 없음      
# print(total)
print(min_length if (min_length != float('inf')) else 0)
