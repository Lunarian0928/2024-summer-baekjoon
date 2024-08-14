import sys
input = sys.stdin.read
data = input().split()

# 선을 그은 횟수
n = int(data[0])
# 각 선분의 좌표에 대한 정보
line = []

index = 1
for _ in range(n):
    # x: 시작점, y: 끝점
    x, y = int(data[index]), int(data[index + 1])
    index += 2
    line.append([x, y])

line.sort()

end_point = line[0][1]
length = line[0][1] - line[0][0]

for i in range(1, n):
    if (line[i][0] < end_point): # 겹치는 부분이 있는가?
        # 겹치는 부분을 넘어선 선분이 있음
        if (line[i][1] > end_point):
            length += line[i][1] - end_point
            end_point = line[i][1]
        # 겹치는 부분만 있음
        else:
            pass
        
    else: # 겹치는 부분이 없음
        length += line[i][1] - line[i][0]
        end_point = line[i][1]
        
print(length)