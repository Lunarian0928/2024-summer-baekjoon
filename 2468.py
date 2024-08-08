from collections import deque

# 큐 생성자
def queue():
    return deque()

# 큐 요소의 개수를 반환
def size(q):
    return len(q)

# 큐가 비어있는지 여부를 반환
def empty(q):
    return (len(q) == 0)

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
# start_x, start_y: 탐색 시작 위치
# zone: 각 지역의 높이를 저장하는 정보
# visited: 탐색할 때 방문하였는지 여부
# h: 침수 높이
# n: 지역의 가로/세로 크기
# dx, dy: 탐색 방향
def bfs(start_x, start_y, zone, visited, h, n, dx, dy):
    q = queue()
    enqueue(q, (start_x, start_y))
    visited[start_y][start_x] = True
    
    while (not empty(q)):
        x, y = dequeue(q)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n):
                if (zone[ny][nx] > h) and (visited[ny][nx] == False):
                    enqueue(q, (nx, ny))
                    visited[ny][nx] = True
                    
# 2차원 배열의 행/열 개수
n = int(input())

# 각 지역의 높이를 저장하는 정보
zone = []
max_height = 0 # 지역 중 최대 높이
for _ in range(n):
    row = list(map(int, input().split()))
    # 지역 중 최대 높이
    max_height = max(max_height, max(row))
    zone.append(row)

# 탐색 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 안전 구역의 최대 개수
max_area_cnt = 1
for h in range(1, max_height + 1):
    # 각 지역을 방문했는지 저장하는 정보
    visited = [[False] * n for _ in range(n)]
    # 침수 높이에 따라 정해지는 안전 구역 수
    area_cnt = 0
    for y in range(0, n):
        for x in range(0, n):
            if (zone[y][x] > h) and (visited[y][x] == False):
                bfs(x, y, zone, visited, h, n, dx, dy)
                area_cnt += 1
    max_area_cnt = max(max_area_cnt, area_cnt)

print(max_area_cnt)