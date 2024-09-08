import sys
input = sys.stdin.read

data = input().split()
# n: ㅅ열의 길이
n = int(data[0])
# 눈덩이의 지름을 저장하는 배열
snow = list(map(int, data[1:]))
snow.sort()

# 두 눈사람의 키 차이 중 최솟값
min_diff_abs = float('inf')

# 이중 반복문을 통해 만들 수 있는 첫번째 눈사람을 구하기
for i in range(n - 1):
    for j in range(i + 1, n):
        snowman1_height = snow[i] + snow[j]

        # 투 포인터 탐색을 통해 만들 수 있는 두 번째 눈사람을 구하기
        start = 0
        end = n - 1
        while start < end:
            # 이미 사용한 눈덩이는 배제하여야 함
            if start == i or start == j:
                start += 1
                continue
            if end == i or end == j:
                end -= 1
                continue
            
            snowman2_height = snow[start] + snow[end]
            diff = snowman1_height - snowman2_height
            min_diff_abs = min(min_diff_abs, abs(diff))
            
            if diff == 0:
                break
            elif diff > 0:
                start += 1
            else:
                end -= 1

print(min_diff_abs)