from collections import deque

# 좌표 클래스
class Point:
    x = 0 # x좌표
    y = 0 # y좌표
    def __init__(self, x, y): # 매개변수 생성자
        self.x = x
        self.y = y

# deque(덱) 요소의 개수를 반환하는 함수
def size(dq): 
    return len(dq)

# deque(덱)이 비어있는지 여부를 반환하는 함수
def empty(dq):
    return 1 if (size(dq) == 0) else 0

# deque(덱)의 front(전단) 요소를 반환하는 함수
def front(dq):
    if (empty(dq)):
        return -1
    return dq[0]

# deque(덱)의 rear(후단)에 요소를 push하는 함수
def enqueue(dq, e):
    dq.append(e)

# deque(덱)의 front(전단) 요소를 제거하고 반환하는 함수
def dequeue(dq):
    if (empty(dq)):
        return -1
    return dq.popleft()

# m: 상자의 가로 칸의 수
# n: 상자의 세로 칸의 수    
m, n = map(int, input().split())

# box: 상자에 저장된 토마토들의 정보
box = [list(map(int, input().split())) for _ in range(n)]
# day: 각 토마토가 익은 날을 저장하는 정보
day = [[0] * m for _ in range(n)]
# dq: 너비 우선 탐색을 위해 사용
dq = deque()

# required_tomato_cnt: 수확해야 하는 토마토의 개수
required_tomato_cnt = m * n

for x in range(m):
    for y in range(n):
        # 토마토가 처음부터 익어있다면
        if (box[y][x] == 1): 
            # 익은 날은 첫쨋날로 설정
            day[y][x] = 1 
            tomato = Point(x, y)
            enqueue(dq, tomato)           
        elif (box[y][x] == -1):
            # 토마토가 들어있지 않은 칸을 반영하여 개수를 업데이트
            required_tomato_cnt -= 1
            
# 탐색해야 하는 방향을 가리킴
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while (not empty(dq)):
    tomato = dequeue(dq)
    x = tomato.x
    y = tomato.y
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n):
            if (box[ny][nx] == 0):
                box[ny][nx] = 1
                day[ny][nx] = day[y][x] + 1
                next_tomato = Point(nx, ny)
                enqueue(dq, next_tomato)        

# total_tomato_cnt: 수확할 수 있는 토마토의 개수
total_tomato_cnt = 0
for x in range(m):
    for y in range(n):
        if (box[y][x] == 1):
            total_tomato_cnt += 1

# 수확해야 하는 토마토의 개수와 수확할 수 있는 토마토의 개수가 같은 경우
# 걸린 날짜를 반환
if (total_tomato_cnt == required_tomato_cnt):
    max_day = 0
    for x in range(m):
        for y in range(n):
            if (max_day < day[y][x]):
                max_day = day[y][x]
    print(max_day - 1)
# 수확에 실패했을 경우
else:
    print(-1)