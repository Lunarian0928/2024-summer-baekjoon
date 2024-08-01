import math

# n: 수학여행에 참가하는 학생 수
# k: 한 방에 배정할 수 있는 최대 인원 수
n, k = map(int, input().split())

# 7: 열의 개수 
# 2: 행의 개수
student = [[0] * 7 for i in range(2)]

for i in range(0, n):
    # s: 학생의 성별
    # y: 학년
    s, y = map(int, input().split())
    student[s][y] += 1

schoolboy = student[0]
schoolgirl = student[1]

room_cnt = 0
for i in range(1, 7):
    room_cnt += math.ceil(schoolboy[i] / k)
    room_cnt += math.ceil(schoolgirl[i] / k)
    
print(room_cnt)