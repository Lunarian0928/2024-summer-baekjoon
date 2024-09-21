import heapq

n = int(input()) # 연산의 개수
min_heap = [] # 최소 힙

result = [] # 답을 저장할 배열
for i in range(n): 
    x = int(input()) 
    if (x != 0): 
        # 오름차순 정렬이되
        # 1순위는 abs(x), 2순위는 x
        heapq.heappush(min_heap, (abs(x), x))
    else:
        if min_heap:
            result.append(heapq.heappop(min_heap)[1])
        else:
            result.append(0)
            
print("\n".join(map(str, result)))