n = list(map(int, input().strip()))
num_cnt = [0 for _ in range(10)]

if (0 not in n) or (sum(n) % 3 != 0):
    print(-1)
    exit()

n.sort(reverse=True)
print(''.join(map(str, n)))