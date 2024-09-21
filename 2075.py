import heapq
n = int(input())

min_heap = []
for _ in range(n):
    row = list(map(int, input().split()))
    for num in row:
        heapq.heappush(min_heap, num)
        
        if (len(min_heap)> n):
            heapq.heappop(min_heap)

print(min_heap[0]) 