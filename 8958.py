# t: 테스트의 개수
t = int(input())

arr = []
for i in range(0, t):
    # score: 더하는 점수
    # total_score: 총점
    score = 0
    total_score = 0
    str = input()
    for ch in str:
        if (ch == 'O'):
            score += 1
            total_score += score
        else:
            score = 0
    arr.append(total_score)
    
for ans in arr:
    print(ans)