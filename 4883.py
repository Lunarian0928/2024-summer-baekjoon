import sys

t = 1

input = sys.stdin.read
data = input().split()
index = 0

while True:
    n = int(data[index]) # 그래프의 행의 개수
    if (n == 0):
        break
    
    graph = []
    index += 1
    for _ in range(n):
        graph.append([int(data[index]), int(data[index + 1]), int(data[index + 2])])
        index += 3
    
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0][0] = float('inf')
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][1] + graph[0][2]
    
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = graph[i][j]
            if (j == 0): # 왼쪽 정점
                dp[i][j] += min(dp[i-1][0], dp[i-1][1])
            elif (j == 1): # 가운데 정점
                dp[i][j] += min(dp[i-1][0], dp[i-1][1], dp[i-1][2], dp[i][0])
            elif (j == 2): # 오른쪽 정점
                dp[i][j] += min(dp[i-1][1], dp[i-1][2], dp[i][1])
    
    print(f'{t}. {dp[n-1][1]}')
    t += 1