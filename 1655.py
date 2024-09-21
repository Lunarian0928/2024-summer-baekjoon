import heapq

n = int(input()) 
min_heap = [] # 중간값보다 큰 값을 저장 (오름차순 정렬)
max_heap = [] # 중간값보다 작거나 같은 값을 저장 (내림차순 정렬)

result = [] # 중간값들을 저장하는 배열

for i in range(n):
    x = int(input()) # 외친 정수
    
    # 처음으로 외친 정수나, 중간값보다 작거나 같은 정수는 max_heap에 저장
    if (len(max_heap) == 0) or (x <= -max_heap[0]):
        heapq.heappush(max_heap, -x) # python에서의 max_heap이므로 음수로 저장
    # 중간값보다 큰 정수는 min_heap에 저장
    else:
        heapq.heappush(min_heap, x) # 
    
    # 중간값을 max_heap[0]으로 만들기 위해서
    # min_heap과 max_heap 크기의 조정이 필요함
    
    # max_heap의 크기는 min_heap보다 커야 함
    # 예시
    # 외친 수의 개수가 1개일 경우 -> len(max_heap) = 1, len(min_heap) = 0
    # 외친 수의 개수가 2개일 경우 -> len(max_heap) = 1, len(min_heap) = 1
    # 외친 수의 개수가 3개일 경우 -> len(max_heap) = 2, len(min_heap) = 1
    # ...
    if (len(max_heap) > len(min_heap) + 1):
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif (len(min_heap) > len(max_heap)):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))  
        
    result.append(-max_heap[0])

print("\n".join(map(str, result)))