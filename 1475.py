import math

# 방 번호에 포함된 각 숫자의 개수
# 인덱스 0번은 1의 개수
arr = [0] * 9

# 방 번호
n = int(input())
n = str(n)

for ch in n:
    arr[ord(ch) - ord('1')] += 1

# 가장 많이 들어있는 숫자를 찾음
max_index = 0
for i in range(1, len(arr)):
    if (arr[max_index] < arr[i]):
        max_index = i

# 만약 가장 많이 들어있는 숫자가 6 혹은 9일 경우
if (max_index == 5) or (max_index == 8):
    # 6이랑 9는 뒤집어서 이용할 수 있음을 반영
    print(math.ceil((arr[5] + arr[8]) / 2))
else:
    print(arr[max_index])