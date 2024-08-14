import heapq 

n = int(input()) # 수업의 개수
lectures = []
for _ in range(n):
    # s: 수업 시작 시간, t: 수업 종료 시간
    s, t = map(int, input().split())
    lectures.append([s, t])

# 강의 시간을 시작 시간 기준으로 오름차순 정렬
# 시작 시간이 같다면 종료 시간을 기준으로 오름차순 정렬
lectures.sort(key=lambda x : x[0])

print(lectures)
# 최소 힙 초기화
heap = []
# 첫 번째 강의의 종료 시간을 힙에 추가
heapq.heappush(heap, lectures[0][1])

for i in range(1, len(lectures)):
    # 현재 강의의 시작 시간이 가장 이른 종료 시간보다 크거나 같으면
    if lectures[i][0] >= heap[0]:
        heapq.heappop(heap) # 기존 강의실을 비움
    
    # 현재 강의의 종료 시간을 힙에 추가
    heapq.heappush(heap, lectures[i][1])
    
print(len(heap))