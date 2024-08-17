n, k = map(int, input().split())

removed = [False for _ in range(n+1)]

remove_cnt = 0
for i in range(2, n+1):
    for j in range(i, n+1, i):
        if (removed[j] == False):
            removed[j] = True
            remove_cnt += 1
            
        if (remove_cnt == k):
            print(j)
            exit()