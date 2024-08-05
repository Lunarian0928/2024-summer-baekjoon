from collections import deque

def queue():
    return deque()

def size(q):
    return len(q)

def empty(q):
    return 1 if (size(q) == 0) else 0

def front(q):
    if (empty(q)):
        return -1
    return q[0]

def rear(q):
    if (empty(q)):
        return -1
    return q[-1] 

def push(q, e):
    return q.append(e)

def pop(q):
    if (empty(q)):
        return -1
    return q.popleft()

n = int(input()) # 카드의 개수
q = queue()

# queue에 1부터 n까지의 수를 push
for i in range(n): 
    push(q, i + 1)
    
while size(q) > 1:
    pop(q) # 제일 위의 카드를 제거
    if (size(q) == 1):
        break
    
    push(q, pop(q)) # 제일 위의 카드를 꺼내어 제일 아래로 옮김
    if (size(q) == 1):
        break

# 남게 되는 카드의 번호를 출력
print(front(q))