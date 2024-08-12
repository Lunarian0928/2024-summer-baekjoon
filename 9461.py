t = int(input()) # 테스트 케이스의 개수

# 테스트 케이스마다 입력받는 정수
num = [0 for _ in range(t)]

# 테스트 케이스마다 정수 입력
for i in range(t):
    num[i] = int(input())   
    
# 가장 큰 정수를 이용해 dp 테이블의 크기를 설정
max_size = max(num) + 1

# 문제에 주어진 기본적인 파도반 수열을 세팅하고자
# max_size는 아무리 작아도 11으로 설정
if (max_size < 11):
    max_size = 11

dp = [0 for _ in range(max_size)]

# 문제에서 주어진 파도반 수열들
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
dp[10] = 9

for i in range(11, max_size):
    dp[i] = dp[i-2] + dp[i-3]

for n in num:
    print(dp[n])