from collections import deque

n = int(input())  # 정점의 개수
graph = [[] for _ in range(n)]

# 그래프 입력
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            graph[i].append(j)

def bfs(start):
    visited = [[False] * n for _ in range(n)]  # n x n 형식으로 초기화
    queue = deque([start])
    if (start in graph[start]):
        visited[start][start] = True  # 자기 자신은 연결됨
    else:
        pass

    while queue:
        point = queue.popleft()
        for neighbor in graph[point]:
            if not visited[start][neighbor]:  # start에서 neighbor로의 연결 여부 체크
                visited[start][neighbor] = True
                queue.append(neighbor)

    return visited[start]  # start 정점에서의 연결 정보 반환

# 연결성 체크
for i in range(n):
    connections = bfs(i)
    for j in range(n):
        print(1 if connections[j] else 0, end=' ')
    print()
