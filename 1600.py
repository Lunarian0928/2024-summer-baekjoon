from collections import deque
import sys

def bfs(k, w, h, grid):    
    # 탐색 시 각 위치에 대한 방문 여부
    visited = [[[False for _ in range(w)] for _ in range(h)] for _ in range(k + 1)]
    # 탐색 시 걸렸던 횟수 정보 
    path = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(k + 1)]

    # 너비 우선 탐색(BFS)에 사용할 큐
    q = deque()
    # 시작점에 대한 방문 여부와 횟수 정보 업데이트
    visited[0][0][0] = True
    path[0][0][0] = 0
    q.append((0, 0, 0))  # 큐에 시작점과 나이트로 움직인 횟수를 삽입
    
    # 탐색 방향
    # 나이트가 이동할 수 있는 경로 + 인접한 칸 이동
    dx = [2, 2, 1, 1, -1, -1, -2, -2, 1, -1, 0, 0] 
    dy = [1, -1, 2, -2, 2, -2, 1, -1, 0, 0, 1, -1]
    
    while q:
        x, y, knight_moved = q.popleft()
        
        if x == w - 1 and y == h - 1:
            return path[knight_moved][y][x]
        
        for i in range(12):
            n_knight_moved = knight_moved
            if i < 8: # 이동방향이 나이트 방향으로 이동할 때
                if knight_moved < k:
                    n_knight_moved += 1 
                else: # 이미 횟수를 다 채웠다면
                    continue # 다음 반복문으로
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < w and 0 <= ny < h:
                if grid[ny][nx] == 0 and not visited[n_knight_moved][ny][nx]:
                    visited[n_knight_moved][ny][nx] = True
                    path[n_knight_moved][ny][nx] = path[knight_moved][y][x] + 1
                    q.append((nx, ny, n_knight_moved))
    
    return -1

# 시간을 줄이기 위해 sys.stdin.read로 한꺼번에 입력받기
input = sys.stdin.read
data = list(map(int, input().split()))
k = data[0] # 나이트로 움직일 수 있는 횟수
w = data[1] # 격자판의 가로 길이
h = data[2] # 격자판의 세로 길이

grid = []
index = 3
for y in range(h):
    row = []
    for x in range(w):
        row.append(data[index])
        index += 1
    grid.append(row)
    
print(bfs(k, w, h, grid))