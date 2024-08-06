from collections import deque
import sys

def queue():
    return deque()

def size(q):
    return len(q)

def empty(q):
    return (size(q) == 0)

def front(q):
    if (empty(q)):
        return -1
    return q[0]

def enqueue(q, e):
    q.append(e)
    
def dequeue(q):
    if (empty(q)):
        return -1
    return q.popleft()

def bfs(start_x, start_y, farm, m, n, dx, dy):
    q = queue()
    enqueue(q, (start_x, start_y))
    farm[start_y][start_x] = 0  # 방문 처리

    while not empty(q):
        x, y = dequeue(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and farm[ny][nx] == 1:
                farm[ny][nx] = 0  # 방문 처리
                enqueue(q, (nx, ny))

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    
    results = []
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for _ in range(t):
        m = int(data[index])
        n = int(data[index + 1])
        k = int(data[index + 2])
        index += 3
        
        farm = [[0] * m for _ in range(n)]
        
        for _ in range(k):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            farm[y][x] = 1
        
        ans = 0
        for y in range(n):
            for x in range(m):
                if farm[y][x] == 1:
                    bfs(x, y, farm, m, n, dx, dy)
                    ans += 1
        
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()