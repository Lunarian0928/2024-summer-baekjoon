import sys
from collections import OrderedDict

input = sys.stdin.read
data = input().split()
index = 0

# k: 수강 가능 인원, l: 수강신청 대기목록의 길이
k, l = int(data[index]), int(data[index + 1])
index += 2

# 수강신청 대기목록
registration = OrderedDict()

for _ in range(l):
    student_id = data[index].strip() # 학번
    index += 1
    # 학번이 대기목록에 있으면
    # 대기목록에서 제거 후 새로 추가
    if student_id in registration:
        del registration[student_id]
    registration[student_id] = None

output = []

for i, student_id in enumerate(registration):
    # 수강 가능 인원이 꽉 찰 경우 반복문 종료
    if i == k:
        break
    output.append(student_id)

# 수강 가능 인원의 학번을 출력
sys.stdout.write("\n".join(output) + "\n")