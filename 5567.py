from collections import deque

n = int(input()) # 동기의 수
m = int(input()) # 리스트의 길이

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    queue = deque([(v, 1)])
    visited[v] = True
    
    while queue:
        student_no, depth = queue.popleft()
        for i in graph[student_no]:
            if (depth <= 2) and (not visited[i]):
                queue.append((i, depth + 1))
                visited[i] = True

bfs(1)
# print(visited)
print(sum(elem for elem in visited[2:]))