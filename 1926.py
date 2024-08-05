from collections import deque

class Point: # 좌표 클래스
    x = 0 # x 좌표 
    y = 0 # y 좌표

    def __init__(self, x, y): # 매개변수 생성자
        self.x = x
        self.y = y
    
    def get_x(self): # x 좌표 반환
        return self.x
    
    def get_y(self): # y 좌표 반환
        return self.y
        
def queue():
    return deque

def size(q):
    return len(q)

def empty(q):
    return (size(q) == 0)

def front(q):
    if (empty(q)):
        return -1
    return q[0]

def rear(q):
    if (empty(q)):
        return - 1
    return q[-1]

def enqueue(q, e):
    q.append(e)

def dequeue(q):
    if (empty(q)):    
        return -1
    return q.popleft()

def check_painting(x, y):
    drawing_paper[x][y] = 0
    dx = [1, -1, 0, 0] # x 축으로의 탐색방향
    dy = [0, 0, 1, -1] # y 축으로의 탐색방향
    area = 1
    q = deque()
    enqueue(q, Point(x, y))

    # queue를 이용하여 가까운 정점만을 확인해
    # 탐색 횟수를 확 줄임
    while (not empty(q)):
        point = dequeue(q)
        x = point.get_x()
        y = point.get_y()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and drawing_paper[nx][ny] == 1:
                enqueue(q, Point(nx, ny))
                drawing_paper[nx][ny] = 0 
                area += 1
    return area
    
n, m = map(int, input().split())
drawing_paper = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if (drawing_paper[i][j] == 1):
            cnt += 1
            max_area = max(check_painting(i, j), max_area)
    
print(cnt)
print(max_area)