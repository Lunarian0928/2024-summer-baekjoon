from collections import deque

def bfs(start, visited):
    queue = deque([start])
    visited[start] = 1  # 시작 정점에 1을 할당
    
    while queue:
        point = queue.popleft()
        for neighbor in neighbors[point]:
            if visited[neighbor] == 0:  # 방문하지 않은 정점
                visited[neighbor] = -visited[point]  # 다른 값으로 설정 (1 -> -1, -1 -> 1)
                queue.append(neighbor)
            # 방문한 정점이면 색깔 확인
            elif visited[neighbor] == visited[point]:  # 인접한 정점이 같은 값이면 이분 그래프 아님
                return False
    return True

result = []    
K = int(input())  # 테스트 케이스의 개수
for _ in range(K):
    V, E = map(int, input().split())  # 정점의 개수: V, 간선의 개수: E
    neighbors = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)  # 0: 방문 안 함, 1: 색 1, -1: 색 -1
    
    for _ in range(E):
        u, v = map(int, input().split())
        neighbors[u].append(v)
        neighbors[v].append(u)
    
    is_bipartite = True
    for i in range(1, V + 1):
        if visited[i] == 0:  # 방문하지 않은 정점이 있으면 BFS로 이분 그래프 확인
            if not bfs(i, visited): # 이분 그래프가 아닌 것으로 판별 나면 flag를 업데이트
                is_bipartite = False
                break

    if is_bipartite:
        result.append("YES")
    else:
        result.append("NO")

print('\n'.join(result))