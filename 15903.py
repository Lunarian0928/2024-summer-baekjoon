import heapq

# n: 카드의 개수를 나타내는 수
# m: 카드 합체의 수
n, m = map(int, input().split())

# 입력된 숫자를 리스트로 받아 heap으로 변환
a = list(map(int, input().split()))
heapq.heapify(a)

fusion_cnt = 0
while (fusion_cnt < m):
    fusion_num = heapq.heappop(a) + heapq.heappop(a)
    
    for _ in range(2):
        heapq.heappush(a, fusion_num)
    
    fusion_cnt += 1
    
print(sum(a))