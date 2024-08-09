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

# 너비 우선 탐색(BFS)
def bfs(n):
    # 탐색 때 방문하였는지 여부
    visited = [False for _ in range(0, n + 1)]
    
    q = queue()
    enqueue(q, n) # 시작 위치를 큐에 삽입하고
    visited[n] = True # 방문 여부를 업데이트
    
    cnt = 0 # 연산 횟수
    while (not empty(q)):
        for _ in range(size(q)):
            x = dequeue(q)
            
            if (x == 1):
                return cnt    
            
            # 연산 1: X가 3으로 나누어 떨어지면, 3으로 나눈다.
            if (x % 3 == 0) and (not visited[x // 3]):
                visited[x // 3] = True
                enqueue(q, x // 3)    
            # 연산 2: X가 2로 나누어 떨어지면, 2로 나눈다.
            if (x % 2 == 0) and (not visited[x // 2]):
                visited[x // 2] = True
                enqueue(q, x // 2)
            # 연산 3: 1을 뺀다
            if (x > 0) and (not visited[x - 1]):
                visited[x - 1] = True
                enqueue(q, x - 1)
        cnt += 1
        
    return cnt

n = int(input())
print(bfs(n))