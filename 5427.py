from collections import deque

# 큐 생성자
def queue():
    return deque()

# 큐 요소의 개수를 반환
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

# 테스트 케이스의 개수
t = int(input())
# 정답을 저장하는 리스트
arr = []

# fired_points: 불이 난 지점
# start_x, start_y: 상근이의 시작 위치
# building_map: 건물 지도 정보
# fired_time: 불이 난 시간 정보
# visited_time: 방문한 시간 정보
# dx, dy: 탐색 방향
# w, h: 건물 지도의 너비와 높이
def bfs(fired_points, start_x, start_y, building_map, fired_time, visited_time, dx, dy, w, h):
    q1 = queue()
    for fired_point in fired_points:
        enqueue(q1, fired_point)
        
    while (not empty(q1)):
        x, y = dequeue(q1)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < w) and (0 <= ny < h):
                # 건물의 빈 공간이고, 불이 붙지 않았었다면
                if (building_map[ny][nx] == '.') and (fired_time[ny][nx] == 0):
                    fired_time[ny][nx] = fired_time[y][x] + 1
                    enqueue(q1, (nx, ny))
    
    q2 = queue()
    enqueue(q2, (start_x, start_y))      
    # 시작 지점이 이미 가장자리인 경우
    if start_x == 0 or start_x == w - 1 or start_y == 0 or start_y == h - 1:
        return 1  
    
    while (not empty(q2)):
        x, y = dequeue(q2)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < w) and (0 <= ny < h):
                # 빈 공간이고, 방문하지 않았던 곳이라면
                if (building_map[ny][nx] == '.') and (visited_time[ny][nx] == 0):
                    # 불이 붙지 않았고, 방문할 때 불이 붙지 않는 곳이라면
                    if (fired_time[ny][nx] == 0 or visited_time[y][x] + 1 < fired_time[ny][nx]):
                        visited_time[ny][nx] = visited_time[y][x] + 1
                        enqueue(q2, (nx, ny))
                        # 가장자리로 벗어나면 탈출 성공
                        if (nx == 0 or nx == w - 1 or ny == 0 or ny == h - 1):
                            return visited_time[ny][nx]
    # 탈출이 불가능한 경우
    return "IMPOSSIBLE"

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(t):
    w, h = map(int, input().split())
    
    start_x, start_y = 0, 0
    building_map = [[0] * w for _ in range(h)]
    
    fired_points = []
    fired_time = [[0] * w for _ in range(h)]
    visited_time = [[0] * w for _ in range(h)]
    
    for y in range(h):
        building_map[y] = list(input().strip())
        for x in range(w):
            if (building_map[y][x] == '@'):
                start_x, start_y = x, y
                visited_time[y][x] = 1
            if (building_map[y][x] == '*'):
                fired_points.append((x, y))
                fired_time[y][x] = 1
    
    result = bfs(fired_points, start_x, start_y, building_map, fired_time, visited_time, dx, dy, w, h)            
    arr.append(result)

for result in arr:
    print(result)