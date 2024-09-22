from collections import deque

# n: 정점의 개수, m: 간선의 개수, v: 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)] # 그래프 인접 리스트
visited1 = [False] * (n + 1) # dfs 방문 여부
visited2 = [False] * (n + 1) # bfs 방문 여부

# 간선 정보 입력받기
for _ in range(m):
    u, w = map(int, input().split())
    graph[u].append(w)
    graph[w].append(u)

# 정점 번호가 작은 것부터 방문하도록 인접 리스트 정렬
for i in range(1, n+1):
    graph[i].sort()

# DFS 함수
def dfs(v):
    print(v, end=' ')
    visited1[v] = True
    for i in graph[v]:
        if not visited1[i]:
            dfs(i)

# BFS 함수
def bfs(v):
    queue = deque([v])
    visited2[v] = True
    while queue:
        next = queue.popleft()
        print(next, end=' ')
        for i in graph[next]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

# DFS와 BFS 호출
dfs(v)  # 시작점 v에서 탐색
print()
bfs(v)  # 시작점 v에서 탐색
print()
