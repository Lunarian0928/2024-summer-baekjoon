from collections import deque
n, m = map(int, input().split())

neighbors = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    neighbors[b].append(a)
    
def bfs(start):
    distances = [0] * (n + 1)
    visited = [False] * (n + 1)
    queue = deque([(start, 1)])
    visited[start] = True
    distances[start] = 1
    
    while queue:
        point, distance = queue.popleft()
        for neighbor in neighbors[point]:
            if (not visited[neighbor]):
                queue.append((neighbor, distance + 1))    
                visited[neighbor] = True
                distances[neighbor] = distance + 1
    return max(distances)

hacked_computer_cnts = [0]
max_hacked_computer_cnt = 0
for i in range(1, n + 1):
    hacked_computer_cnt = bfs(i)
    hacked_computer_cnts.append(hacked_computer_cnt)
    max_hacked_computer_cnt = max(max_hacked_computer_cnt, hacked_computer_cnt)
    
print(*(i for i in range(1, n + 1) if hacked_computer_cnts[i] == max_hacked_computer_cnt), end=' ')