from collections import deque

def queue():
    return deque()

def size(q):
    return len(q)

def empty(q):
    return (size(q) == 0)

def front(q):
    if (empty(q)):
        return None
    return q[0]

def enqueue(q, e):
    q.append(e)
    
def dequeue(q):
    if (empty(q)):
        return None
    else:
        return q.popleft()
        
def bfs(start_x, start_y, end_x, end_y, board, l, dx, dy):
    q = queue()
    enqueue(q, (start_x, start_y))
    visited[start_y][start_x] = 1
    
    while (not empty(q)):
        x, y = dequeue(q)
        
        if (x == end_x and y == end_y):
            return board[y][x]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
                    
            if (0 <= nx < l) and (0 <= ny < l):
                if (visited[ny][nx] == 0):
                    visited[ny][nx] = 1
                    board[ny][nx] = board[y][x] + 1
                    enqueue(q, (nx, ny))
    return -1

t = int(input()) # 테스트 케이스의 개수
arr = [] # 정답
for _ in range(t):
    l = int(input()) # 체스판의 한 변의 길이
    board = [[0] * l for _ in range(l)] 
    visited = [[0] * l for _ in range(l)]

    start_x, start_y = map(int, input().split()) # 시작점
    end_x, end_y = map(int, input().split()) # 도착점

    # 나이트가 이동할 수 있는 경로
    dx = [-2, -2, -1, -1, 1, 1, 2, 2] 
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    # 나이트가 움직여야 하는 횟수
    arr.append(bfs(start_x, start_y, end_x, end_y, board, l, dx, dy))

for ans in arr:
    print(ans)