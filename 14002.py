n = int(input()) # 수열의 크기
a = list(map(int, input().split())) # 수열

# 인덱스별 가장 길게 증가하는 부분 수열의 길이
dp = [0 for _ in range(n)]

# 동적 프로그래밍을 통해 
# 부분 수열의 길이를 계산
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if (a[j] < a[i]):
            dp[i] = max(dp[i], dp[j] + 1)


order = max(dp) # 가장 긴 부분 수열의 길이를 저장
print(order)
# 부분 수열 (거꾸로 저장됨)
subseq = [] 

for i in range(n - 1, -1, -1):
    if (dp[i] == order):
        subseq.append(a[i])
        order -= 1
    
    if (order == 0): 
        break


for num in subseq[::-1]:
    print(num, end = ' ')