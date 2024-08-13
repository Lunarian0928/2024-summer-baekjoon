import sys
input = sys.stdin.read
data = input().split()

index = 0

n, m = int(data[index]), int(data[index + 1])

index = 2
matrix = []
# 표에 숫자를 입력
for _ in range(n):
    row = []
    for _ in range(n):
        row.append(int(data[index]))
        index += 1
    matrix.append(row)

dp = [[0 for _ in range(n)] for _ in range(n)]

for y in range(n):
    for x in range(n):
        dp[y][x] += dp[y][x-1] + matrix[y][x]
         
ans = []
for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    value = 0
    if (y1 == y2) and (x1 == x2):
        value = matrix[y1-1][x1-1]
    else:
        for y in range(y1-1, y2):
            value += dp[y][n-1]
            for x in range(x1-1):
                value -= matrix[y][x]
    
    ans.append(value)

for value in ans:
    print(value)