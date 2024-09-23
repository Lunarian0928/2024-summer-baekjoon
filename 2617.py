from collections import deque
# n: 구슬의 개수, m: 저울에 올려 본 쌍의 개수
n, m = map(int, input().split())

neighbors1 = [[] for _ in range(n + 1)] # 더 가벼운 것
neighbors2 = [[] for _ in range(n + 1)] # 더 무거운 것
for _ in range(m):
    m1, m2 = map(int, input().split())
    neighbors1[m1].append(m2)
    neighbors2[m2].append(m1)
    
def bfs(start):
    visited1 = [False] * (n + 1)
    visited2 = [False] * (n + 1)
    queue1 = deque([start])
    queue2 = deque([start])
    visited1[start] = True
    visited2[start] = True
    while (queue1):
        point = queue1.popleft()
        for neighbor in neighbors1[point]:
            if (not visited1[neighbor]):
                visited1[neighbor] = True
                queue1.append(neighbor)
    while (queue2):
        point = queue2.popleft()
        for neighbor in neighbors2[point]:
            if (not visited2[neighbor]):
                visited2[neighbor] = True
                queue2.append(neighbor)
            
    return visited1, visited2

# 구슬의 개수가 3개라고 하면
# 중간 구슬이 되기 위해서는 해당 구슬보다 작은 구슬이 1개, 큰 구슬이 1개 있어야 함.

cnt = 0
# 구슬의 개수가 5개라고 하면
# 중간 구슬이 되기 위해서는 해당 구슬보다 작은 구슬이 2개, 큰 구슬이 2개 있어야 함.
for i in range(1, n + 1):
    visited1, visited2 = bfs(i)
    lighter_marble_cnt = sum(1 for elem in visited1 if elem) - 1
    heavier_marble_cnt = sum(1 for elem in visited2 if elem) - 1
    # print(f"{i}번 구슬보다 가벼운 구슬의 개수: {lighter_marble_cnt}")
    # print(f"{i}번 구슬보다 무거운 구슬의 개수: {heavier_marble_cnt}")
    if (lighter_marble_cnt > (n - 1) // 2) or (heavier_marble_cnt > (n - 1) // 2):
        # print("중간값 될 수 없음")
        cnt += 1

print(cnt)