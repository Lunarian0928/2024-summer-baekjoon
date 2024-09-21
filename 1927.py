import heapq

result = []
min_heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if (x > 0):
        heapq.heappush(min_heap, x)
    elif (x == 0):
        if min_heap:
            result.append(heapq.heappop(min_heap))
        else:
            result.append(0)
    
print('\n'.join(map(str, result)))