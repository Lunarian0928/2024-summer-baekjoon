t = int(input()) # 테스트 케이스의 개수
ans = []
for _ in range(t):
    n = int(input()) # 동전의 가지 수
    coin = list(map(int, input().split()))
    m = int(input()) # 동전으로 만들어야 할 금액
    
    dp = [0 for _  in range(m + 1)]
    dp[0] = 1
    
    for price in coin:
        for i in range(1, m + 1):   
            if (i - price >= 0):         
                dp[i] += dp[i - price]
    
    ans.append(dp[m])

for value in ans:
    print(value)