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
    else:
        return q[0]
    
# 큐의 rear(후단)에 요소를 삽입
def enqueue(q, e):
    q.append(e)
    
# 큐의 front(전단) 요소를 반환
def dequeue(q):
    if (empty(q)):
        return None
    return q.popleft()
            
# 너비 우선 탐색(BFS) 탐색
def bfs(start_x, start_y, graph_paper, n, m, dx, dy):
    q = queue()
    enqueue(q, (start_x, start_y))
    graph_paper[start_y][start_x] = 1
    
    area = 0
    while (not empty(q)):
        x, y = dequeue(q)
        area += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m):
                if (graph_paper[ny][nx] == 0):
                    graph_paper[ny][nx] = 1
                    enqueue(q, (nx, ny))
                    
    return area
# m: 모눈종이의 세로
# n: 모눈종이의 가로
# k: 직사각형의 개수
m, n, k = map(int, input().split())

# 모눈 종이
graph_paper = [[0] * n for _ in range(m)]

# 각 직사각형의 좌표가 저장되어 있는 리스트
rects = []
for _ in range(k):
    rect = list(map(int, input().split()))
    rects.append(rect)

    for x in range(rect[0], rect[2]):
        for y in range(rect[1], rect[3]):
            graph_paper[y][x] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0 # 분리되어 나누어지는 영역의 개수
areas = [] # 분리되어 나누어지는 영역의 넓이
for y in range(m):
    for x in range(n):
        if (graph_paper[y][x] == 0):
            cnt += 1
            area = bfs(x, y, graph_paper, n, m, dx, dy)
            if (area > 0):
                areas.append(area)

print(cnt)
areas.sort()
for area in areas: 
    print(area, end = ' ')