from collections import deque 

def is_empty(queue):
    return len(queue) == 0
    
max_size = 100000  # 5자리 비밀번호까지 고려
is_prime = [True for _ in range(max_size)]
is_prime[0] = is_prime[1] = False
primes = []

for i in range(2, max_size):
    if is_prime[i]:
        for j in range(i * 2, max_size, i):
            is_prime[j] = False

def bfs(start, end):
    if start == end:
        return 0  # 시작과 끝이 같으면 거리는 0
    
    queue = deque([(start, 0)])
    visited = [False for _ in range(max_size)]
    visited[start] = True
    
    while not is_empty(queue):
        pw, cnt = queue.popleft()
        str_pw = str(pw)
        
        if pw == end:
            return cnt
        
        for i in range(4):
            for j in range(10):  # 0부터 9까지 시도
                if i == 0 and j == 0:
                    continue  # 첫 자리에서 0으로 시작할 수 없음
                str_new_pw = str_pw[:i] + str(j) + str_pw[i+1:]
                new_pw = int(str_new_pw)
                if new_pw < max_size and not visited[new_pw] and is_prime[new_pw]:
                    visited[new_pw] = True
                    queue.append((new_pw, cnt + 1))
    
    return -1

t = int(input())
for _ in range(t):
    start, end = map(int, input().split())
    min_cnt = bfs(start, end)
    if (min_cnt == -1):
        print("Impossible")
    else:
        print(min_cnt)
