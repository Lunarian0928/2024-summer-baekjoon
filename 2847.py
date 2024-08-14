n = int(input())
score = []

for _ in range(n):
    score.append(int(input()))

ans = 0
high_score = score[-1]

for level in range(n-2, -1, -1):
    # print(f'score[{level}]: {score[level]}')
    # print(f'high_score: {high_score}')
    if (score[level] >= score[level+1]):
        while True:
            score[level] -= 1
            ans += 1
            if (score[level] < score[level+1]):
                break

# print(score)
print(ans)