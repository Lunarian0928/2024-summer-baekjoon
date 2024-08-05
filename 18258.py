from collections import deque
import sys
input = sys.stdin.read

def queue():
    return deque()

def push(queue, e):
    queue.append(e)

def pop(queue):
    if (not empty(queue)):
        return queue.popleft()
    else:
        return -1
        
def size(queue):
    return len(queue)

def empty(queue):
    return 1 if (len(queue) == 0) else 0

def front(queue):
    if (not empty(queue)):
        return queue[0]
    else:
        return -1
    
def back(queue):
    if (not empty(queue)):
        return queue[-1]
    else:
        return -1
    
q = queue()
data = input().split()
n = int(data[0])
index = 1
for _ in range(n):
    cmd = data[index]
    if cmd == "push":
        push(q, int(data[index + 1]))
        index += 2
    elif cmd == "pop":
        print(pop(q))
        index += 1
    elif cmd == "size":
        print(size(q))
        index += 1
    elif cmd == "empty":
        print(empty(q))
        index += 1
    elif cmd == "front":
        print(front(q))
        index += 1
    elif cmd == "back":
        print(back(q))
        index += 1