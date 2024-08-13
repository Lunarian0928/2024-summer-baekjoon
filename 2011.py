code = input().strip()

# 암호가 '0'으로 시작할 경우 해석 불가
if code[0] == '0':
    print(0)
    exit(0)

arr = list(map(int, code))
n = len(arr)

dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

divisor = 10 ** 6

for i in range(2, n + 1):
    single_digit = arr[i - 1]
    double_digit = arr[i - 2] * 10 + arr[i - 1]

    # 1자리 문자를 제외한 앞의 i-1 문자를 표현하는 방법
    if 1 <= single_digit <= 9:
        dp[i] += dp[i - 1]
        dp[i] %= divisor
        
    # 2자리 문자를 제외한 앞의 i-2 문자를 표현하는 방법
    if 10 <= double_digit <= 26:
        dp[i] += dp[i - 2]
        dp[i] %= divisor

print(dp[-1])