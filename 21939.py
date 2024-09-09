import heapq

n = int(input())  # 문제의 개수

max_heap = []
min_heap = []
cnt = {}

for _ in range(n):
    # 문제 번호: p, 난이도: l
    p, l = map(int, input().split())
    heapq.heappush(max_heap, (-l, -p))  # 최대 힙: 난이도를 음수로 저장하고, 문제 번호를 음수로 저장
    heapq.heappush(min_heap, (l, p))   # 최소 힙: 난이도를 그대로 저장하고, 문제 번호는 그대로 저장
    
    if p in cnt:
        cnt[p] += 1
    else:
        cnt[p] = 1

result = []
m = int(input())  # 명령문의 개수

for _ in range(m):
    command = list(input().split())  # 명령문
    operation = command[0]
    
    if operation == 'recommend':
        x = int(command[1])
        if x == 1:  # 최댓값을 출력
            while max_heap and cnt.get(-max_heap[0][1], 0) == 0:
                heapq.heappop(max_heap)
            if max_heap:
                result.append(-max_heap[0][1])  # 음수로 저장된 문제 번호를 양수로 변환
        elif x == -1:  # 최솟값을 출력
            while min_heap and cnt.get(min_heap[0][1], 0) == 0:
                heapq.heappop(min_heap)
            if min_heap:
                result.append(min_heap[0][1])  # 문제 번호를 그대로 사용
                
    elif operation == 'add':
        # 문제 번호: p, 난이도: l
        p, l = int(command[1]), int(command[2])
        heapq.heappush(max_heap, (-l, -p))  # 최대 힙: 난이도를 음수로 저장하고, 문제 번호를 음수로 저장
        heapq.heappush(min_heap, (l, p))   # 최소 힙: 난이도를 그대로 저장하고, 문제 번호는 그대로 저장
        
        if p in cnt:
            cnt[p] += 1
        else:
            cnt[p] = 1
            
    elif operation == 'solved':
        # 문제 번호: p
        p = int(command[1])
        
        if p in cnt:
            cnt[p] -= 1
            if cnt[p] == 0:
                del cnt[p]
                
        while max_heap and cnt.get(-max_heap[0][1], 0) == 0:
            heapq.heappop(max_heap)
        while min_heap and cnt.get(min_heap[0][1], 0) == 0:
            heapq.heappop(min_heap)    

print("\n".join(map(str, result)))