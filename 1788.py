import sys

n = int(sys.stdin.read())

# 제수
divisor = 10**9

abs_n = abs(n)

# n = 0일 경우
if n == 0:
    print(0)
    print(0)
    sys.exit()

# n이 양수일 경우 피보나치 수열 계산
if n > 0:
    dp1, dp2 = 0, 1  # F(0) = 0, F(1) = 1
    for i in range(2, abs_n + 1):
        dp1, dp2 = dp2, (dp1 + dp2) % divisor
    result = dp2

# n이 음수일 경우 피보나치 수열 계산
else:
    dp1, dp2 = 0, 1  # F(0) = 0, F(1) = 1
    for i in range(2, abs_n + 1):
        dp1, dp2 = dp2, (dp1 + dp2) % divisor
    # F(-n) = (-1)^(n+1) * F(n)
    result = dp2 if abs_n % 2 != 0 else -dp2

# F(-1) = 1 * F(1) = F(1) = 1
# F(-2) = -1 * F(2) = -F(2) = -1
# F(-3) = 1 * F(3) = F(3) = 2

# 부호 출력
if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)

# 피보나치 수열 값의 절댓값 출력
print(abs(result))