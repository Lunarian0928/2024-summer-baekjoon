from collections import deque
import sys

def queue():
    return deque()

def size(q):
    return len(q)

def empty(q):
    return size(q) == 0

def enqueue(q, e):
    q.append(e)
    
def dequeue(q):
    if empty(q):
        return -1
    return q.popleft()    

def bfs(start_x, start_y, start_z, tomato, day, m, n, h, dx, dy, dz):
    q = queue()
    enqueue(q, (start_x, start_y, start_z))
    day[start_z][start_y][start_x] = 1 
    
    while not empty(q):
        x, y, z = dequeue(q)
        for i in range(6):  
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            if (0 <= nx < m) and (0 <= ny < n) and (0 <= nz < h):
                if tomato[nz][ny][nx] == 0:  # Unripe tomato
                    tomato[nz][ny][nx] = 1
                    day[nz][ny][nx] = day[z][y][x] + 1
                    enqueue(q, (nx, ny, nz))

def main():    
    input = sys.stdin.read()
    data = input().split()
    index = 0
    
    m = int(data[index]) 
    n = int(data[index + 1]) 
    h = int(data[index + 2]) 
    
    index += 3
    tomato = []
    day = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    
    required_tomato_cnt = 0
    
    for z in range(h):
        level = []
        for y in range(n):
            row = list(map(int, data[index:index + m]))  # Convert the row to integers
            level.append(row)
            for x in range(m):
                if row[x] == 1:
                    required_tomato_cnt += 1
                    day[z][y][x] = 1
                elif row[x] == -1:
                    day[z][y][x] = -1
            index += m
        tomato.append(level)
    
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]   
    
    total_tomato_cnt = 0
    max_day = 0        
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if tomato[z][y][x] == 1:
                    total_tomato_cnt += 1
                    bfs(x, y, z, tomato, day, m, n, h, dx, dy, dz)
                max_day = max(max_day, day[z][y][x])
    
    if required_tomato_cnt != total_tomato_cnt:
        print(-1)
    else:
        print(max_day - 1)

if __name__ == "__main__":
    main()