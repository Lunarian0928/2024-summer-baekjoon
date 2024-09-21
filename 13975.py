import heapq

result = []
t = int(input()) # 테스트 데이터의 개수
for _ in range(t):
    min_heap = []
    k = int(input()) # 소설을 구성하는 장의 수
    chapters = list(map(int, input().split())) # 입력 값을 리스트로 변환
    for chapter in chapters:
        heapq.heappush(min_heap, chapter)
    
    total_cost = 0
    while len(min_heap) >= 2:
        first = heapq.heappop(min_heap)
        second = heapq.heappop(min_heap)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(min_heap, cost)
    result.append(total_cost)
    
print('\n'.join(map(str, result)))