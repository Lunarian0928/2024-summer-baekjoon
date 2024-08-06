from collections import deque

# 좌표를 표현하는 Point 클래스 정의
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# BFS 함수 정의
def bfs(maze, start, n, m):
    queue = deque([start])  # BFS 탐색을 위한 큐 초기화 및 시작 지점 추가
    distances = [[0] * m for _ in range(n)]  # 각 지점까지의 거리를 저장하는 배열 초기화
    distances[start.x][start.y] = 1  # 시작 지점의 거리 설정

    # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:  # 큐가 비어있지 않은 동안 반복
        point = queue.popleft()  # 큐에서 현재 지점을 꺼냄
        x, y = point.x, point.y

        for i in range(4):  # 네 방향으로 이동을 시도
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 이동할 좌표가 미로 범위 내에 있는지 확인
                if maze[nx][ny] == 1 and distances[nx][ny] == 0:  # 이동할 수 있는 길이고 아직 방문하지 않은 경우
                    distances[nx][ny] = distances[x][y] + 1  # 현재 지점까지의 거리 + 1을 저장
                    queue.append(Point(nx, ny))  # 이동할 지점을 큐에 추가
                    if nx == n - 1 and ny == m - 1:  # 도착 지점에 도달한 경우
                        return distances[nx][ny]  # 최단 경로 길이 반환
    return -1  # 도착 지점에 도달할 수 없는 경우

# 이동해야 하는 좌표 (n, m) 입력 받기
n, m = map(int, input().split())

# 미로 정보 입력 받기
maze = [list(map(int, input().strip())) for _ in range(n)]

# 시작 지점 설정
start_point = Point(0, 0)

# BFS를 사용하여 최단 경로를 찾고 결과 출력
shortest_path_length = bfs(maze, start_point, n, m)
print(shortest_path_length)