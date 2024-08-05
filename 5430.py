import sys
from collections import deque

def size(dq):
    return len(dq)

def empty(dq):
    return 1 if (size(dq) == 0) else 0

def front(dq):
    if empty(dq):
        return -1
    return dq[0]

def back(dq):
    if empty(dq):
        return -1
    return dq[-1]
        
def push_front(dq, e):
    dq.appendleft(e)

def push_back(dq, e):
    dq.append(e)
    
def pop_front(dq):
    if empty(dq):
        return -1
    else:
        return dq.popleft()

def pop_back(dq):
    if empty(dq):
        return -1
    else:
        return dq.pop()

# 첫 번째 수를 버리는 함수
def discard(dq, reverse_flag):
    if (not reverse_flag):
        return pop_front(dq)
    return pop_back(dq)

input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

results = []

for _ in range(t):
    p_list = data[index]
    index += 1
    
    n = int(data[index])
    index += 1
    
    arr = data[index].strip()
    index += 1
    
    if n > 0:
        arr = arr[1:-1]  # 대괄호 제거
        if arr:
            num = list(map(int, arr.split(',')))
        else:
            num = []
        dq = deque(num)
    else:
        dq = deque()
    
    error_occurred = False
    reverse_flag = False
    for p in p_list:
        if p == 'R':
            reverse_flag = not reverse_flag
        elif p == 'D':
            res = discard(dq, reverse_flag)
            if res == -1:
                error_occurred = True
                break
    
    if error_occurred:
        results.append("error")
    else:
        results.append(f"[{','.join(map(str, dq))}]")

print("\n".join(results))