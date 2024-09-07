from collections import defaultdict 

# n: 수열의 길이, k: 같은 정수를 k개 이하로 포함하여야 함
n, k = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
cnt = 0 # 연속 부분 수열의 길이
max_cnt = 0 # 최장 연속 부분 수열의 길이

# 부분 수열에서 특정 원소가 몇 개 포함되어 있는지 세기 위함
dictionary = defaultdict(int)

for end in range(n):
    dictionary[arr[end]] += 1 # 원소의 개수를 업데이트
    cnt += 1
    
    # 특정 원소의 개수가 k개를 넘어갔을 때
    while (dictionary[arr[end]] > k):    
        dictionary[arr[start]] -= 1 # 슬라이딩 윈도우를 축소
        cnt -= 1
        start += 1
    
    max_cnt = max(max_cnt, cnt)
    
print(max_cnt)