from collections import deque
import sys

def bfs(m, n, k, matrix):
    # 벽을 부순 횟수와 위치에 따른 방문 여부
    visited = [[[False] * m for _ in range(n)] for _ in range(k + 1)]
    
    q = deque([(0, 0, 0)])  # (x, y, wall_breaked)
    visited[0][0][0] = True
    dist = 1  # BFS의 거리 시작점

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while q:
        for _ in range(len(q)):  # 현재 큐의 크기만큼 반복
            x, y, wall_breaked = q.popleft()
            
            if x == m - 1 and y == n - 1:
                return dist
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[ny][nx] == 0 and not visited[wall_breaked][ny][nx]:
                        visited[wall_breaked][ny][nx] = True
                        q.append((nx, ny, wall_breaked))
                    elif matrix[ny][nx] == 1 and wall_breaked < k and not visited[wall_breaked + 1][ny][nx]:
                        visited[wall_breaked + 1][ny][nx] = True
                        q.append((nx, ny, wall_breaked + 1))
        
        dist += 1  # 한 층 탐색 후 거리 증가
    
    return -1

# Input processing
input = sys.stdin.read
data = input().split()

index = 0
n = int(data[index])
m = int(data[index + 1])
k = int(data[index + 2])

matrix = []
index = 3
for _ in range(n):
    row = list(map(int, data[index]))
    matrix.append(row)
    index += 1

print(bfs(m, n, k, matrix))