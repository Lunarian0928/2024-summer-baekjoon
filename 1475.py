import math

# 방 번호에 포함된 각 숫자의 개수
arr = [0] * 10

# 방 번호 입력
n = input()

# 각 숫자의 개수를 센다
for ch in n:
    arr[int(ch)] += 1

# 6과 9는 뒤집어서 사용할 수 있으므로 합쳐서 평균을 구함
six_nine_count = arr[6] + arr[9]
arr[6] = arr[9] = math.ceil(six_nine_count / 2)

print(max(arr))