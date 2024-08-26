a, b = map(int, input().split())

seq = []
cnt = 0

for i in range(1, 46):
    for j in range(0, i):
        seq.append(i)
        cnt += 1
        
        if (cnt == 1000):
            break
    if (cnt == 1000):
        break

print(sum(seq[a-1:b]))