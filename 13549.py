from collections import deque

def size(dq):
    return len(dq)

def empty(dq):
    return (len(dq) == 0)

def bfs(start_pos, end_pos, time):
    visited = [False for _ in range(0, max_size + 1)]
        
    dq = deque()
    visited[start_pos] = True
    time[start_pos] = 0
    dq.append(start_pos)
    
    while (not empty(dq)):
        pos = dq.popleft()
        
        # 현재 위치가 목표 위치인 경우
        if pos == end_pos:
            return time[pos]
            
        teleport_pos = pos * 2
        if (0 <= teleport_pos <= max_size) and not visited[teleport_pos]:
            visited[teleport_pos] = True
            time[teleport_pos] = time[pos]
            dq.appendleft(teleport_pos)
            
        backward_pos = pos - 1
        if (0 <= backward_pos <= max_size) and not visited[backward_pos]:
            visited[backward_pos] = True
            time[backward_pos] = time[pos] + 1
            dq.append(backward_pos)
            
        forward_pos = pos + 1
        if (0 <= forward_pos <= max_size) and not visited[forward_pos]:
            visited[forward_pos] = True
            time[forward_pos] = time[pos] + 1
            dq.append(forward_pos)

    return -1
    
# n: 수빈이의 위치, k: 동생의 위치
n, k = map(int, input().split())
max_size = 100000
time = [0 for _ in range(0, max_size + 1)]
print(bfs(n, k, time))