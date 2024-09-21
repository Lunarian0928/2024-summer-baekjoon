import heapq
max_heap = [] # 최대 힙

result = []
n = int(input()) # 연산의 개수
for _ in range(n):
    x = int(input()) # 자연수 x
    if (x != 0):
        heapq.heappush(max_heap, -x)
    else:
        # 배열이 비어있지 않은 경우 가장 큰 값을 추가
        if max_heap:
            result.append(-heapq.heappop(max_heap))
        # 배열이 비어있는 경우 0을 추가
        else:
            result.append(0)

print('\n'.join(map(str, result)))