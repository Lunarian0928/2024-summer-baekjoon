# n: 세로의 길이, m: 가로의 길이
n, m = map(int, input().split())

matrix = []
# dp[i][j]: 세로로 i+1번째, 가로로 j+1번째에서 가장 긴 정사각형에서의 길이
dp = [[0 for _ in range(m)] for _ in range(n)]

for y in range(n):
    row = list(map(int, input().strip()))
    matrix.append(row)
    for x in range(m):
        if row[x] == 1:
            dp[y][x] = 1  

ans = 0
for y in range(n):  
    for x in range(m):
        if matrix[y][x] == 1:
            if y > 0 and x > 0:
                # 좌상단, 좌측, 상단의 dp 값을 이용해 dp[y][x] 갱신
                dp[y][x] = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1]) + 1
            ans = max(ans, dp[y][x])

print(ans ** 2)  # 정사각형의 넓이를 출력