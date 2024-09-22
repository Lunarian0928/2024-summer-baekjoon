from collections import deque

n, m = map(int, input().split())
neighbors = [[] for _  in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    neighbors[b].append(a)

def bfs(start):
    distances = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        point, distance = queue.popleft()
        for neighbor in neighbors[point]:
            if (not visited[neighbor]):
                distances[neighbor] = distance + 1
                visited[neighbor] = True
                queue.append((neighbor, distance + 1))
    
    return distances
    
distances = bfs(1)
max_distance = max(distances) # 숨어야 하는 헛간까지의 거리

# 숨어야 하는 헛간 번호를 출력
for i in range(1, n + 1):
    if (distances[i] == max_distance):
        print(i, end = ' ')
        break
    
print(max_distance, end = ' ') 
# 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력
print(distances[1:].count(max_distance))