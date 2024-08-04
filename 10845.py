# 시간 복잡도를 줄이기 위한 데크(deque)
from collections import deque 
import sys # sys 모듈
# 표준 입력을 한 번에 받을 수 있도록 함
# 파일의 끝까지 한번에 읽어오고 읽은대로 출력
input = sys.stdin.read 

# queue 생성자
def queue():
    return deque()

# rear(후단) 쪽으로 queue에 요소를 push
def push(q, e):
    q.append(e)

# front(전단) 값을 queue에서 제거하고 반환
def pop(q):
    if not empty(q):
        return q.popleft()
    else:
        return -1

# queue에 들어있는 정수의 개수를 반환
def size(q):
    return len(q)

# queue가 비어있는지 여부를 반환
def empty(q):
    return 1 if size(q) == 0 else 0

# queue의 front(전단) 값을 반환
def front(q):
    if empty(q):
        return -1
    return q[0]

# queue의 rear(후단) 값을 반환
def back(q):
    if empty(q):
        return -1
    return q[-1]

q = queue()

data = input().split()
n = int(data[0])
index = 1
for _ in range(n):
    cmd = data[index]
    if cmd == 'push':
        push(q, int(data[index + 1]))
        index += 2
    elif cmd == 'pop':
        print(pop(q))
        index += 1
    elif cmd == 'size':
        print(size(q))
        index += 1
    elif cmd == 'empty':
        print(empty(q))
        index += 1
    elif cmd == 'front':
        print(front(q))
        index += 1
    elif cmd == 'back':
        print(back(q))
        index += 1