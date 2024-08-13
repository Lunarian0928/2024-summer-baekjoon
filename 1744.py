import math
n = int(input()) # 수열의 크기

seq = []
for _ in range(n):
    seq.append(int(input()))

seq.sort(key=lambda x: math.fabs(x), reverse=True)

ans = 0
i = 0

while (i < n):
    
    if (i + 1 < n):
        value = seq[i] * seq[i + 1]
        if (value > 0) and (not seq[i] == seq[i + 1] == 1):
            ans += value
            i += 2
        elif (value == 0) and ((seq[i] < 0) or (seq[i + 1] < 0)):
            ans += value
            i += 2
        else:
            ans += seq[i]
            i += 1
    else:
        ans += seq[i]
        i += 1
    print(f'i: {i}, ans: {ans}')
print(ans)