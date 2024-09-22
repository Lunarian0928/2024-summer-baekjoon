n, m = map(int, input().split()) # n: 정점의 개수, m: 간선의 개수
graph = [[] for _ in range(n+1)] # 그래프 인접 리스트
visited = [False] * (n + 1) # 방문 체크 리스트

for _ in range(m):
    # u: 간선의 시작점, v: 간선의 끝점
    u, v = map(int, input().split())
    # 점 u와 연결되어 있는 점 v를 추가
    graph[u].append(v)
    # 점 v와 연결되어 있는 점 u를 추가
    graph[v].append(u)

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if (not visited[i]):
            dfs(i)

# 연결 요소의 개수 세기
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)