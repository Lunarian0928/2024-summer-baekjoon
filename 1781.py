import heapq
problems = [] # 숙제 목록

n = int(input()) # 숙제의 개수
for i in range(n):
    num = i + 1 
    deadline, cup_ramen = map(int, input().split())
    problems.append((deadline, cup_ramen))
problems.sort() # 데드라인 순서대로 정렬

heap = [] # 최소 힙
total_cup_ramen = 0 # 받을 수 있는 최대 컵라면 수
# 마감일, 컵라면 수
for deadline, cup_ramen in problems: 
    heapq.heappush(heap, cup_ramen)
    
    # 현재 힙에 들어있는 요소가 deadline을 초과한다면
    # (문제를 푸는데 단위시간 1이 걸리므로 가능한 방법)
    if (len(heap) > deadline):
        heapq.heappop(heap)
        
print(sum(heap))