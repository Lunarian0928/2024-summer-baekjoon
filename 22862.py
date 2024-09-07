# n: 수열의 길이, k: 삭제할 수 있는 최대 횟수
n, k = map(int, input().split())
# 수열 s
s = list(map(int, input().split()))

start = 0
even_len = 0 # 부분 수열의 길이
max_even_len = 0 # 최대 부분 수열의 길이
removed_cnt = 0

for end in range(n):
    if (s[end] % 2 == 0):
        even_len += 1
    else:
        removed_cnt += 1
    
    while (removed_cnt > k):
        if (s[start] % 2 == 0):
            even_len -= 1
        else:
            removed_cnt -= 1
        start += 1
    
    max_even_len = max(max_even_len, even_len)

print(max_even_len)