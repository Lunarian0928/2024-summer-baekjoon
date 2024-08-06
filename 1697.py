from collections import deque

class Position:
    def __init__(self, x, time):
        self.x = x
        self.time = time

def queue():
    return deque()

def size(q):
    return len(q)

def empty(q):
    return len(q) == 0

def front(q):
    if empty(q):
        return -1
    return q[0]

def enqueue(q, e):
    q.append(e)

def dequeue(q):
    if empty(q):
        return -1
    return q.popleft()

def walk_forward(n):
    return n + 1

def walk_backward(n):
    return n - 1

def teleport(n):
    return n * 2

# n: 수빈이가 있는 위치
# k: 동생이 있는 위치
n, k = map(int, input().split())
q = queue()

# 문제에서 주어지는 범위를 초과하지 않도록 설정
max_size = 100001  # 문제에서 주어지는 위치의 최대 값 (0 <= n, k <= 100000)
shortest_path = [float('inf')] * max_size

# 수빈이가 있는 처음 위치는 0초!
shortest_path[n] = 0
enqueue(q, Position(n, 0))

while not empty(q):
    pos = dequeue(q)
    x = pos.x
    time = pos.time

    if x == k:
        print(time)
        break

    # 앞으로 걸었을 경우
    ntime = time + 1
    nx = walk_forward(x)
    if nx < max_size and ntime < shortest_path[nx]:
        shortest_path[nx] = ntime
        enqueue(q, Position(nx, ntime))

    # 뒤로 걸었을 경우
    nx = walk_backward(x)
    if nx >= 0 and ntime < shortest_path[nx]:  # 위치가 음수가 되지 않도록 확인
        shortest_path[nx] = ntime
        enqueue(q, Position(nx, ntime))

    # 순간이동을 하는 경우
    nx = teleport(x)
    if nx < max_size and ntime < shortest_path[nx]:
        shortest_path[nx] = ntime
        enqueue(q, Position(nx, ntime))