length = 5
# 동적으로 리스트 생성
scores = list(range(0, length))

sum = 0
for i in range(0, length):
    scores[i] = int(input())
    # 문제 조건에 맞춰 특정 학생은 40점으로 설정
    if (scores[i] < 40):
        scores[i] = 40 
    sum += scores[i]

print(sum // length) # 평균