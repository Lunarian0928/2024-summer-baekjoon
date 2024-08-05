from collections import deque
import math

def size(dq):
    return len(dq)

def empty(dq):
    return 1 if (size(dq) == 0) else 0

def front(dq):
    if (empty(dq)):
        return -1
    return dq[0]

def back(dq):
    if (empty(dq)):
        return -1
    return dq[-1]

def push_front(dq, e):
    dq.appendleft(e)
    
def push_back(dq, e):
    dq.append(e)
    
def pop_front(dq):
    if (empty(dq)):
        return -1
    return dq.popleft()
    
def pop_back(dq):
    if (empty(dq)):
        return -1
    return dq.pop()

# 양방향 순환 큐의 요소들을 왼쪽으로 한 칸 이동시킴
def move_left(dq):
    push_back(dq, pop_front(dq))
    
# 3번째 기능
# 양방향 순환 큐의 요소들을 오른쪽으로 한 칸 이동시킴 
def move_right(dq):
    push_front(dq, pop_back(dq))
    
dq = deque()
# n: 양방향 순환 큐의 원소 개수
# m: 뽑아내야 하는 순의 개수
n, m = map(int, input().split())

for i in range(n):
    push_back(dq, i + 1)

# pos: 뽑아내려고 하는 수의 위치들    
pos = list(map(int, input().split()))
# elem: 뽑아내려고 하는 값들
elem = [-1] * m

for i in range(m):
    elem[i] = dq[pos[i] - 1]
    
left_moved = 0 # 2번 연산을 한 횟수
right_moved = 0 # 3번 연산을 한 횟수
for i in range(m):
    # 뽑고자 하는 원소
    cur = elem[i]

    # dist1: 뽑고자 하는 원소의 위치와 front 사이의 거리
    dist1 = math.fabs(dq.index(cur) - 0) 
    # dist2: 뽑고자 하는 원소의 위치와 rear 사이의 거리
    dist2 = math.fabs(size(dq) - 1 - dq.index(cur))
    
    while (cur != front(dq)):
        if (dist1 <= dist2):
            move_left(dq)
            left_moved += 1
        else:
            move_right(dq)
            right_moved += 1
    pop_front(dq)
# 2번, 3번 연산의 최솟값을 출력
print(left_moved + right_moved)