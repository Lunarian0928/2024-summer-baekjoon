from collections import deque
# n: 유저의 수, m: 친구 관계의 수
n, m = map(int, input().split())

# 그래프 인접 목록
neighbors = [[] for _ in range(n + 1)]
for _ in range(m): 
    a, b = map(int, input().split()) 
    neighbors[a].append(b)
    neighbors[b].append(a)
    
# 너비 우선 탐색(bfs)
def bfs(start):
    visited = [False] * (n + 1) # 방문 여부
    distances = [float('inf')] * (n + 1) # 방문 횟수
    
    queue = deque([(start, 0)]) 
    visited[start] = True
    distances[start] = 0
    
    while queue:
        point, distance = queue.popleft()
        
        for neighbor in neighbors[point]:    
            if (not visited[neighbor]):
                queue.append((neighbor, distance + 1))
                visited[neighbor] = True
                distances[neighbor] = distance + 1
    
    return distances

# 케빈 베이컨(kevin_bacon): 모든 distance의 합 중 가장 작은 값
min_kevin_bacon = float('inf') 
kevin_bacons = [0] 
for i in range(1, n + 1):
    kevin_bacon = sum(bfs(i)[1:])
    kevin_bacons.append(kevin_bacon)
    min_kevin_bacon = min(min_kevin_bacon, kevin_bacon)

for i in range(1, n + 1):
    # 케빈 베이컨의 수가 가장 작은 사람을 확인
    if (kevin_bacons[i] == min_kevin_bacon):
        print(i) # 사람의 번호를 출력
        break