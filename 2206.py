from collections import deque

def queue():
    return deque()

def size(q):
    return len(q)

def empty(q):
    return (len(q) == 0)

def front(q):
    if (empty(q)):
        return None
    return q[0]

def enqueue(q, e):
    q.append(e)
    
def dequeue(q):
    if (empty(q)):
        return None
    return q.popleft()

def bfs(start_x, start_y, matrix, n, m, dx, dy):
    q = queue() 
    enqueue(q, (start_x, start_y, 0))  # (x, y, 벽을 부순 횟수)
    visited = [[[False, False] for _ in range(m)] for _ in range(n)]  # [벽을 부수지 않고 방문, 벽을 부수고 방문]
    visited[start_y][start_x][0] = True # 시작 위치는 방문한 것으로 처리
    path = [[[0, 0] for _ in range(m)] for _ in range(n)]  # [벽을 부수지 않았을 때 경로 정보, 벽을 부쉈을 때 경로 정보]
    path[start_y][start_x][0] = 1 # 시작 위치의 경우도 경로에 포함해야 함
    
    while q:
        x, y, wall_break_count = q.popleft()
        
        if x == m - 1 and y == n - 1:
            return path[y][x][wall_break_count]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n:
                # 빈 공간이고, 방문하지 않은 곳이었다면
                if matrix[ny][nx] == 0 and not visited[ny][nx][wall_break_count]:
                    visited[ny][nx][wall_break_count] = True 
                    path[ny][nx][wall_break_count] = path[y][x][wall_break_count] + 1
                    q.append((nx, ny, wall_break_count))
                
                # 벽이 있고, 벽을 부수지 않았으며, 방문하지 않은 곳이었다면
                if matrix[ny][nx] == 1 and wall_break_count == 0 and not visited[ny][nx][1]:
                    visited[ny][nx][1] = True
                    path[ny][nx][1] = path[y][x][wall_break_count] + 1
                    q.append((nx, ny, 1))
    
    return -1

# n: 행렬의 세로 길이
# m: 행렬의 가로 길이
n, m = map(int, input().split())

matrix = []  # 각 위치별 정보

for y in range(n):
    row = list(map(int, input().strip()))
    matrix.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = bfs(0, 0, matrix, n, m, dx, dy)
print(result)