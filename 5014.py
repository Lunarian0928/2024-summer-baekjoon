from collections import deque

def queue():
    return deque()

def size(q):
    return len(q)

def empty(q):
    return (len(q) == 0)

def front(q):
    if (empty(q)):
        return None
    return q[0]

def enqueue(q, e):
    q.append(e)

def dequeue(q):
    if (empty(q)):
        return None
    return q.popleft()

# f: 건물의 층 수
# s: 현위치
# g: 목적지
# u: 위로 올라갈 수 있는 층 단위 
# d: 아래로 내려갈 수 있는 층 단위
# btn_cnt: 각 층에 도달하기 위해 눌러야 하는 버튼의 횟수 정보
def bfs(f, s, g, u, d, btn_cnt, visited):
    q = queue()
    enqueue(q, s)
    btn_cnt[s] = 0
    visited[s] = True
    
    while (not empty(q)):
        level = dequeue(q)
        if (level == g):
            return btn_cnt[level]
        
        up_level, down_level = level + u, level - d
        if (up_level >= 1) and (up_level <= f) and (visited[up_level] == False):
            btn_cnt[up_level] = btn_cnt[level] + 1
            visited[up_level] = True
            enqueue(q, up_level)

        if (down_level >= 1) and (down_level <= f) and (visited[down_level] == False):
            btn_cnt[down_level] = btn_cnt[level] + 1
            visited[down_level] = True
            enqueue(q, down_level)
    return -1
    
# f: 건물의 층 수
# s: 현위치
# g: 목적지
# u: 위로 올라갈 수 있는 층 단위 
# d: 아래로 내려갈 수 있는 층 단위
f, s, g, u, d = map(int, input().split())
max_size = f

# 각 층에 도달하기 위해 눌러야 하는 버튼의 횟수 정보
btn_cnt = [0 for _ in range(0, f * 2)]
visited = [False for _ in range(0, f * 2)]

ans = bfs(f, s, g, u, d, btn_cnt, visited)
if (ans == -1):
    print("use the stairs")
else:
    print(ans)