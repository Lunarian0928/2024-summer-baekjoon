from collections import deque

# 큐 생성자
def queue():
    return deque()

# 큐에 들어있는 요소의 개수를 반환
def size(q):
    return len(q)

# 큐가 비어있는지 여부를 반환
def empty(q):
    return (size(q) == 0)

# 큐의 front(전단) 요소를 반환
def front(q):
    if (empty(q)):
        return None
    return q[0]

# 큐의 rear(후단)에 요소를 삽입
def enqueue(q, e):
    q.append(e)
    
# 큐의 front(전단) 요소를 제거하고 반환    
def dequeue(q):
    if (empty(q)):
        return None
    return q.popleft()

# 너비 우선 탐색(BFS)
# start_x, start_y: 탐색 시작 지점
# matrix: 빙산이 차지하는 칸과 높이 정보를 저장
# visited: 탐색 중 방문 여부
# m: 행렬의 가로 크기, n: 행렬의 세로 크기
def bfs(start_x, start_y, matrix, visited, m, n):
    q = queue()
    enqueue(q, (start_x, start_y))
    visited[start_y][start_x] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while (not empty(q)):
        x, y = dequeue(q)
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < m) and (0 <= ny < n) and not visited[ny][nx]:
                if matrix[ny][nx] > 0:
                    visited[ny][nx] = True
                    enqueue(q, (nx, ny))

# 빙산이 분리되었는지 확인하는 함수
# matrix: 빙산이 차지하는 칸과 높이 정보를 저장
# m: 열의 크기, n: 행의 크기
def check_separated(matrix, m, n):
    # visited: 탐색 시 방문하였는지 정보
    visited = [[False] * m for _ in range(n)]
    # 분리된 구역의 수
    area_cnt = 0
    
    for y in range(n):
        for x in range(m):
            if matrix[y][x] > 0 and not visited[y][x]:
                bfs(x, y, matrix, visited, m, n)
                area_cnt += 1
                
    return area_cnt

# 빙산의 높이를 변형시키는 함수
# matrix: 빙산이 차지하는 칸과 높이 정보를 저장
# m: 열의 크기, n: 행의 크기
def melt(matrix, m, n):
    # 각 칸의 빙산이 녹는 높이 정보
    melted_height = [[0] * m for _ in range(n)]
    
    # 탐색 방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for y in range(n):
        for x in range(m):
            if matrix[y][x] > 0:
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    # 빙산의 동서남북 방향을 확인하며 바다가 있을 경우
                    if 0 <= nx < m and 0 <= ny < n and matrix[ny][nx] == 0:
                        # 빙산의 녹는 높이를 증가
                        melted_height[y][x] += 1
    
    for y in range(n):
        for x in range(m):
            # 빙산의 녹는 높이를 반영
            matrix[y][x] -= melted_height[y][x]
            # 빙산에 저장된 높이는 0보다 줄어들 수 없음
            if matrix[y][x] < 0:
                matrix[y][x] = 0

# n: 행의 크기, m: 열의 크기
n, m = map(int, input().split())

# 빙산이 차지하는 칸과 높이 정보를 저장
matrix = [list(map(int, input().split())) for _ in range(n)]

year = 0 # 빙산이 분리되는 최초의 시간
while True:
    # 빙산이 녹게 되어 matrix를 업데이트하는 함수
    melt(matrix, m, n) 
    year += 1 # 연도를 1년 증가
    
    # area_cnt: 분리된 빙산의 개수    
    area_cnt = check_separated(matrix, m, n)
    
    # 빙산이 다 녹아 area_cnt가 0개가 될 경우
    if area_cnt == 0: 
        print(0)
        break
    # 빙산이 일부분 녹아 area_cnt가 1개보다 많을 경우
    if area_cnt > 1:
        print(year)
        break