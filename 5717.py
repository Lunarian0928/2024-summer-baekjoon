arr = []
while True:
    # m: 상근이의 남자 친구 수
    # f: 상근이의 여자 친구 수
    m, f = map(int, input().split())
    if (m == 0) and (f == 0):
        break
    arr.append(m + f)

for ans in arr:
    print(ans)