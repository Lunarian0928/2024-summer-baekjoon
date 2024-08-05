from collections import deque
import sys
input = sys.stdin.read

# deque(덱)에 들어있는 정수의 개수를 반환
def size(dq):
    return len(dq)

# deque(덱)이 비어있으면 1을, 아니면 0을 반환
def empty(dq):
    return 1 if (size(dq) == 0) else 0

# deque(덱)의 front(가장 앞)에 있는 정수를 반환
def front(dq):
    if (empty(dq)):
        return -1
    return dq[0]

# deque(덱)의 rear(가장 뒤)에 있는 정수를 반환
def back(dq):
    if (empty(dq)):
        return -1
    return dq[-1]

# deque(덱)의 front(가장 앞)에 요소를 push
def push_front(dq, e):
    dq.appendleft(e)

# deque(덱)의 rear(가장 뒤)에 요소를 push
def push_back(dq, e):
    dq.append(e)

# deque(덱)의 front(가장 앞)에 있는 요소를 빼고, 그 수를 반환
def pop_front(dq):
    if (empty(dq)):
        return -1
    return dq.popleft()

# deque(덱)의 rear(가장 뒤)에 있는 요소를 빼고, 그 수를 반환
def pop_back(dq):
    if (empty(dq)):
        return -1
    return dq.pop()

data = input().split()
n = int(data[0])
index = 1

dq = deque()
for i in range(n):
    cmd = data[index]
    if (cmd == "push_front"):
        push_front(dq, int(data[index + 1]))
        index += 2
    elif (cmd == 'push_back'):
        push_back(dq, int(data[index + 1]))
        index += 2
    elif (cmd == 'pop_front'):
        print(pop_front(dq))
        index += 1
    elif (cmd == 'pop_back'):
        print(pop_back(dq))
        index += 1
    elif (cmd == 'size'):
        print(size(dq))
        index += 1
    elif (cmd == 'empty'):
        print(empty(dq))
        index += 1
    elif (cmd == 'front'):
        print(front(dq))
        index += 1
    elif (cmd == 'back'):
        print(back(dq))
        index += 1