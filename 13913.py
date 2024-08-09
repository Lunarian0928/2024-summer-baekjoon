from collections import deque

# 큐 생성자
def queue():
    return deque()

# 큐에 들어있는 요소의 개수를 반환
def size(q):
    return len(q)

# 큐가 비어있는지 여부를 반환
def empty(q):
    return (len(q) == 0)

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

# 너비 우선 탐색(BFS)
def bfs(n, k):
    max_size = 100000
    # 방문 여부 정보
    visited = [False] * (max_size + 1) 
    # 방문에 걸린 시간 정보
    time = [-1] * (max_size + 1)
    # 경로를 역추적하기 위해 부모를 기록
    parent = [-1] * (max_size + 1)  

    q = queue()
    # 시작 위치에 대해 업데이트
    enqueue(q, n)
    visited[n] = True
    time[n] = 0

    while q:
        pos = q.popleft()
        
        # 동생을 찾았을 경우
        if pos == k: 
            path = []
            while pos != -1:
                path.append(pos) # 현재 위치와
                pos = parent[pos] # 그 바로 이전 위치를 저장
                # 이를 반복
            # path의 경우 거꾸로 들어갔기 때문에, 인덱싱을 통해 리스트를 역순화
            return time[k], path[::-1]

        # 뒤로 걸을 경우
        backward_pos = pos - 1
        if 0 <= backward_pos <= max_size and not visited[backward_pos]:
            visited[backward_pos] = True
            time[backward_pos] = time[pos] + 1
            parent[backward_pos] = pos # 바로 이전의 위치를 저장
            q.append(backward_pos)

        # 앞으로 걸을 경우
        forward_pos = pos + 1
        if 0 <= forward_pos <= max_size and not visited[forward_pos]:
            visited[forward_pos] = True
            time[forward_pos] = time[pos] + 1
            parent[forward_pos] = pos # 바로 이전의 위치를 저장
            q.append(forward_pos)

        # 순간이동 할 경우
        teleport_pos = pos * 2
        if 0 <= teleport_pos <= max_size and not visited[teleport_pos]:
            visited[teleport_pos] = True
            time[teleport_pos] = time[pos] + 1
            parent[teleport_pos] = pos # 바로 이전의 위치를 저장
            q.append(teleport_pos)

    return -1

# n: 수빈이의 위치, k: 동생의 위치
n, k = map(int, input().split())
max_size = 100000
time = [0 for _ in range(max_size + 1)]

min_time, path = bfs(n, k)

print(min_time)
for num in path:
    print(num, end = ' ')