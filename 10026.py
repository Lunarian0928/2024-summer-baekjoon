from collections import deque
import sys
import copy

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

# start_x: 탐색을 시작하는 위치의 x 좌표
# start_y: 탐색을 시작하는 위치의 y 좌표
# values: 특정 구역에 속하는 값
# area: 그리드의 정보
# n: 그리드의 가로/세로 크기
# dx: x축의 탐색 방향
# dy: y축의 탐색 방향
def bfs(start_x, start_y, values, area, n, dx, dy):
    q = queue()
    enqueue(q, (start_x, start_y))
    area[start_y][start_x] = 'X'
    
    while (not empty(q)):
        x, y = dequeue(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and area[ny][nx] in values:
                area[ny][nx] = 'X' # 방문했던 영역을 표시
                enqueue(q, (nx, ny))        

def main():    
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0]) # n: 그리드의 가로/세로 크기
    
    # area1: 적록색약이 아닌 사람이 바라보는 그리드 정보
    area1 = []
    index = 1
    for i in range(n):
        area1.append(list(data[index + i]))
    
    # area2: 적록색약인 사람이 바라보는 그리드 정보
    area2 = copy.deepcopy(area1)

    # dx: x축의 탐색 방향
    # dy: y축의 탐색 방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # area_cnt1: 적록색약이 아닌 사람이 바라봤을 떄 구역의 수
    area_cnt1 = 0
    # area_cnt2: 적록색약인 사람이 바라봤을 때 구역의 수
    area_cnt2 = 0
    
    for y in range(n):
        for x in range(n):
            # 적록색약이 아닌 사람이 바라봤을 때의 BFS
            if area1[y][x] in 'RGB':
                bfs(x, y, [area1[y][x]], area1, n, dx, dy)
                area_cnt1 += 1
            # 적록색약인 사람이 바라봤을 때의 BFS1
            if area2[y][x] in 'RG':
                bfs(x, y, ['R', 'G'], area2, n, dx, dy)
                area_cnt2 += 1
            # 적록색약인 사람이 바라봤을 때의 BFS2
            elif area2[y][x] == 'B':
                bfs(x, y, ['B'], area2, n, dx, dy)
                area_cnt2 += 1

    # 구역의 수를 공백으로 구분해 출력
    print(f"{area_cnt1} {area_cnt2}")

if __name__ == "__main__":
    main()
