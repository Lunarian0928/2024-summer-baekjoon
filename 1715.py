import heapq

n = int(input())
min_heap = []

for _ in range(n):
    bundle = int(input())
    heapq.heappush(min_heap, bundle)
    
compairson_cnt = 0


while len(min_heap) >= 2:
    first = heapq.heappop(min_heap)
    second = heapq.heappop(min_heap)
    
    cost = first + second
    compairson_cnt += cost
    
    heapq.heappush(min_heap, cost)

print(compairson_cnt)