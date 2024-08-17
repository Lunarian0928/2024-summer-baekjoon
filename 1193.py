import math

# x 입력 받기
x = int(input())

# x를 만족하는 대각선 번호 계산 (삼각수 공식 사용)
diag_num = math.ceil((-1 + math.sqrt(1 + 8 * x)) / 2)

# 해당 대각선의 삼각수 값 계산
dp_value = diag_num * (diag_num + 1) // 2
value = dp_value - x

# 대각선 번호에 따라 분수 출력
if diag_num % 2 == 0:
    print(f'{diag_num - value}/{1 + value}')
else:
    print(f'{1 + value}/{diag_num - value}')