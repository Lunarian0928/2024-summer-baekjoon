def dp(n, table):
    for i in range(2, n + 1):
        # 현재 수에서 1을 빼는 경우는
        # 이전의 수에서 1을 더한 횟수에 1을 더한 것이다.
        # ex) table[2] = table[1] + 1
        table[i] = table[i - 1] + 1
        
        if i % 2 == 0:
            # 현재 수에서 1을 뺐던 경우와 2로 나누어 떨어지는 경우 중
            # 최단 코스트를 계산
            table[i] = min(table[i], table[i // 2] + 1)
        if i % 3 == 0:
            # 현재 수에서 1을 뺐던 경우와 3으로 나누어 떨어지는 경우 중
            # 최단 코스트를 계산
            table[i] = min(table[i], table[i // 3] + 1)

n = int(input())
max_size = n + 1
table = [0] * max_size

dp(n, table)
print(table[n]) 