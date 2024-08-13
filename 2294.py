import sys
input = sys.stdin.read

data = input().split()
index = 0

# n: 동전의 종류, k: 만들어야 하는 가치의 합
n, k = int(data[index]), int(data[index + 1])

# 각 동전의 가치 정보
coin = []
coin.append(0)

# 동전의 가치 입력
index = 2
for _ in range(n):
    coin.append(int(data[index]))
    index += 1
    
dp = [float('inf') for _ in range(k + 1)]
# 0원을 만들기 위해 동전은 0개 필요함
dp[0] = 0

# 1원부터 k원까지 확인하면서
for money in range(1, k + 1):
    # 각 동전의 가치를 확인함
    for price in coin:
        if (money - price >= 0):
            # money원을 만들기 위한 동전의 개수는 
            # money - price원을 만들기 위한 동전의 개수에 price원 동전 1개를 더한 것임
            dp[money] = min(dp[money], dp[money - price] + 1)

ans = dp[-1]

# 만약 k원을 만들기 불가능하다면
if (ans == float('inf')):
    print(-1)
else:
    print(ans)