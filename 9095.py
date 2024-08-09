t = int(input()) # 테스트 케이스의 개수
max_size = 10 # 가능한 정수 최댓값
# 다이나믹 프로그래밍(DP)에 사용할 테이블
table = [0 for _ in range(max_size + 1)]

table[1] = 1
# 1
table[2] = 2 
# 1+1
# 2
table[3] = 4
# 1+1+1
# 1+2, 2+1
# 3
table[4] = 7
# 1+1+1+1
# 1+1+2, 1+2+1, 2+1+1
# 2+2
# 1+3, 3+1

for i in range(5, max_size + 1):
    # table[i - 3]: 주어진 케이스에서 뒤에 +3을 붙이면 i가 나옴
    # table[i - 2]: 주어진 케이스에서 뒤에 +2를 붙이면 i가 나옴
    # table[i - 1]: 주어진 케이스에서 뒤에 +1을 붙이면 i가 나옴
    table[i] = table[i - 3] + table[i - 2] + table[i - 1]

for _ in range(t):
    n = int(input())
    print(table[n])