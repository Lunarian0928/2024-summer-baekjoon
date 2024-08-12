# n: 동전의 개수
# k: 만들어야 하는 가치의 합
n, k = map(int, input().split())
# 각각의 동전이 나타내는 가치 정보
coin = [0 for _ in range(n)]

# 동전 가치 입력
for i in range(n):
    coin[i] = int(input())
    
# dp[i]는 동전의 합이 i원이 되도록 하는 경우의 수
dp = [0 for _ in range(k + 1)] 
# dp[0]은 동전을 0개 사용했을 때 만들 수 있으므로, 1이라고 설정
dp[0] = 1

for price in coin:
    for money in range(1, k + 1):
        if (money - price >= 0):
            dp[money] += dp[money - price]
            
print(dp[k])