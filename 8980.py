# n: 마을 수, c: 트럭의 용량을 입력받음
n, c = map(int, input().split())

# 보내는 박스 정보의 개수를 입력받음
m = int(input()) 

# 테이블 리스트를 초기화
table = []
for _ in range(m):
    # 출발지, 도착지, 박스 개수를 입력받아 테이블에 추가
    dep, dest, capacity = map(int, input().split())
    table.append([dep, dest, capacity])

# 도착지를 기준으로 테이블을 정렬
table.sort(key=lambda x: (x[1]))

# 옮긴 전체 박스 개수를 기록할 변수
total_box_cnt = 0

# 각 마을의 트럭 용량을 초기화 (초기에는 모두 최대 용량 c)
box = [c for _ in range(n+1)] 

# 테이블의 각 정보를 순회하며 처리
for dep, dest, capacity in table:
    # 현재 구간에서 옮길 수 있는 박스의 최대 개수(_min)를 계산
    _min = min(box[dep:dest])
    _min = min(_min, capacity)
    
    # 옮길 수 있는 최대 박스 개수를 total_box_cnt에 더함
    total_box_cnt += _min

# 최종적으로 옮길 수 있는 전체 박스 개수를 출력
print(total_box_cnt)