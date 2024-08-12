n = int(input()) # 삼각형의 크기
matrix = [] # 삼각형의 정보(2차원 리스트)

for _ in range(n):
    # 각 층의 숫자 정보를 추가
    matrix.append(list(map(int, input().split())))

# dp[i][j]: 삼각형 i+1층에서의 j+1번째 수를 선택했을 떄 선택된 수의 최대 합
dp = [[0 for _ in range(n)] for _ in range(n)]
# 삼각형 꼭대기에서의 dp 값은 꼭대기 숫자 값
dp[0][0] = matrix[0][0]

for i in range(1, n):
    for j in range(i+1):
        # dp[i-1][j]: 오른쪽 위에서의 dp 최댓값
        # dp[i-1][j-1]: 왼쪽 위에서의 dp 최댓값
        dp[i][j] = max(dp[i-1][j] + matrix[i][j], dp[i-1][j-1] + matrix[i][j])
        
print(max(dp[n-1]))