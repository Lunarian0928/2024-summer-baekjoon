n, k = map(int, input().split())
bino_coef = [[0 for _ in range(n+1)] for _ in range(n+1)]
bino_coef[0][0] = 1

divisor = 10007
for i in range(1, n+1):
    bino_coef[i][0] = bino_coef[i][i] = 1
    for j in range(1, i):
        bino_coef[i][j] = bino_coef[i-1][j-1] + bino_coef[i-1][j]
        bino_coef[i][j] %= divisor
print(bino_coef[n][k])