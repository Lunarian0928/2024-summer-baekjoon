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

def bfs(start_x, start_y, apartment_map, n, dx, dy):
    q = queue()
    enqueue(q, (start_x, start_y))
    apartment_map[start_y][start_x] = 0
    
    cnt = 0
    while (not empty(q)):
        x, y = dequeue(q)
        cnt += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and (apartment_map[ny][nx] == 1):
                apartment_map[ny][nx] = 0
                enqueue(q, (nx, ny))
                
    return cnt     
                
n = int(input()) # 지도의 크기
# 좌표별 집이 있는지 여부를 표시한 정보
apartment_map = []

# 좌표별 집이 있는지 입력
for y in range(n):
    row = list(map(int, input().strip()))
    apartment_map.append(row)

# BFS(너비 우선 탐색) 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, - 1]

cnts = [] # 각 단지내 집의 수

for y in range(n):
    for x in range(n):
        if (apartment_map[y][x] == 1):
            cnt = bfs(x, y, apartment_map, n, dx, dy)
            if (cnt > 0):
                cnts.append(cnt)
                
cnts.sort()

print(len(cnts)) # 총 단지 수
# 각 단지내 집의 수를 오름차순으로 출력
for cnt in cnts:
    print(cnt)