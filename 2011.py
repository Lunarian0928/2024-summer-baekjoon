code = input().strip()

arr = list(map(int, code))

dp = [1 for _ in range(len(code) + 1)]
dp[1] = 1

divisor = 10 ** 6 # 제수
for i in range(2, len(code) + 1):
    single_digit = arr[i - 1]
    double_digit = arr[i - 2] * 10 + arr[i - 1]
    
    if 1 <= single_digit <= 9:
        # 1자리 문자를 제외한 앞의 i-1 문자를 표현하는 방법
        dp[i] += dp[i - 1] 
        dp[i] %= divisor
    if 10 <= double_digit <= 26:
        # 2자리 문자를 제외한 앞의 i-2 문자를 표현하는 방법
        dp[i] += dp[i - 2]
        dp[i] %= divisor
        
print(dp[-1])