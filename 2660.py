from collections import deque

n = int(input())  # 회원의 수
neighbors = [[] for _ in range(n + 1)]

while True:
    n1, n2 = map(int, input().split())
    if (n1 == -1) and (n2 == -1):
        break
    neighbors[n1].append(n2)
    neighbors[n2].append(n1)

def bfs(start):
    visited = [False] * (n + 1)
    distances = [float('inf')] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True
    distances[start] = 0 # 본인은 0점
    
    while queue:
        point, dist = queue.popleft()
        
        for neighbor in neighbors[point]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))

    return distances

min_scores = []
for i in range(1, n + 1):
    paths = bfs(i)
    # 자기 자신을 제외하고 최댓값을 찾기
    max_score = max(path for j, path in enumerate(paths[1:], start=1) if j != i and path != float('inf'))
    
    # 한 명이라도 관계가 형성되지 않으면 회장이 될 수 없음
    if all(paths[j] != float('inf') for j in range(1, n + 1) if j != i):
        min_scores.append((i, max_score))

# 최소 점수를 가진 회장 후보 찾기
if min_scores:
    min_candidate_score = min(score for _, score in min_scores)
    candidates = [i for i, score in min_scores if score == min_candidate_score]

    print(min_candidate_score, len(candidates))
    print(' '.join(map(str, candidates)))
else:
    print(0, 0)  # 후보가 없는 경우