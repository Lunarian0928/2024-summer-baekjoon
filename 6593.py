from collections import deque

# 큐 생성자
def queue():
    return deque()

# 큐 요소의 개수를 반환
def size(q):
    return len(q)

# 큐가 비어있는지 여부를 반환
def empty(q):
    return size(q) == 0

# 큐의 front(전단) 요소를 반환
def front(q):
    return q[0] if not empty(q) else None

# 큐의 rear(후단)에 요소를 삽입
def enqueue(q, e):
    q.append(e)

# 큐의 front(전단) 요소를 제거하고 반환
def dequeue(q):
    return q.popleft() if not empty(q) else None

# 너비 우선 탐색(BFS)
# start_x, start_y, start_z: 탐색 시작 위치
# end_x, end_y, end_z: 탐색 종료 위치
# building_map: 각 위치에 대한 분류
# visited: 각 위치에 방문했는지 여부를 저장
# time: 각 위치에 방문한 시간을 저장
# l: 층 수, r: 행 수, c: 열 수
# dx, dy, dz: 탐색 방향
def bfs(start_x, start_y, start_z, end_x, end_y, end_z, building_map, visited, time, l, r, c, dx, dy, dz):
    q = queue()
    visited[start_z][start_y][start_x] = True
    enqueue(q, (start_x, start_y, start_z))
    
    while not empty(q):
        x, y, z = dequeue(q)
        # 인접한 6개의 칸을 탐색
        # 동, 서, 남, 북, 상, 하 
        for i in range(6): 
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            
            if (nx == end_x) and (ny == end_y) and (nz == end_z):
                return time[z][y][x] + 1 # 탈출한 시간을 반환
            
            if (0 <= nx < c) and (0 <= ny < r) and (0 <= nz < l):
                if building_map[nz][ny][nx] == '.' and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = True
                    time[nz][ny][nx] = time[z][y][x] + 1
                    enqueue(q, (nx, ny, nz))
    
    return -1

# 탐색 방향
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

arr = [] # 정답 리스트

while True:
    # l: 층 수, r: 행 수, c: 열 수
    l, r, c = map(int, input().split())
    
    if l == 0 and r == 0 and c == 0:
        break
    
    # building_map: 각 위치에 대한 분류
    building_map = [] 
    # visited: 각 위치에 방문했는지 여부를 저장
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    # time: 각 위치에 방문한 시간을 저장
    time = [[[0] * c for _ in range(r)] for _ in range(l)]

    # start_x, start_y, start_z: 탐색 시작 위치
    # end_x, end_y, end_z: 탐색 종료 위치
    start_x = start_y = start_z = -1
    end_x = end_y = end_z = -1
    
    for z in range(l):
        level = [list(input().strip()) for _ in range(r)]
        building_map.append(level)
        for y in range(r):
            for x in range(c):
                if level[y][x] == 'S': # 시작 지점을 저장
                    start_x, start_y, start_z = x, y, z
                elif level[y][x] == 'E': # 탈출 지점을 저장
                    end_x, end_y, end_z = x, y, z

        # 다음 레벨 사이에 빈 줄이 있을 수 있으므로 읽어주기
        input()  # 빈 줄을 읽어들임

    # 탈출한 시간을 너비 우선 탐색(BFS)를 통해 구함
    escaped_time = bfs(start_x, start_y, start_z, end_x, end_y, end_z, building_map, visited, time, l, r, c, dx, dy, dz)
    arr.append(escaped_time)
    
for ans in arr:
    if (ans < 0):
        print("Trapped!")
    else:
        print(f"Escaped in {ans} minute(s).")