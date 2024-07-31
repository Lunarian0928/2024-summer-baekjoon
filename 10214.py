t = int(input())

arr = []
for i in range(0, t):
    # 해당 경기의 연세대/고려대 득점
    total_score1 = 0
    total_score2 = 0
    ans = ""
    for j in range(0, 9):
        # 해당 회의 연세대/고려대 득점
        score1, score2 = map(int, input().split())
        total_score1 += score1
        total_score2 += score2
        # 연세대가 이긴 경우
        if (total_score1 > total_score2):
            ans = "Yonsei"
        # 고려대가 이긴 경우
        elif (total_score1 < total_score2):
            ans = "Korea"
        # 비긴 경우
        else:
            ans = "Draw"
    arr.append(ans)

for ans in arr:
    print(ans)