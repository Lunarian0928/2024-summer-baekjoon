from collections import Counter
# Counter: 각 요소와 그 요소의 개수를 매핑한 딕셔너리처럼 작동

# n: 멀티탭 구멍의 개수, k: 전기 용품의 총 사용횟수
n, k = map(int, input().split())

# 주어진 리스트
elec_appliance = list(map(int, input().split()))

# 요소의 개수를 세기
count = Counter(elec_appliance)

in_use_cnt = 0
in_use_outlet = set()

pulled_out_cnt = 0
for i in range(k):
    appliance = elec_appliance[i]
    # 이미 전기용품 플러그가 꽂아져 있다면
    if appliance in in_use_outlet:
        continue
    
    # 플러그 꽂을 데가 남아 있다면
    if (in_use_cnt < n):
        in_use_cnt += 1
        in_use_outlet.add(appliance)
    # 플러그 꽂을 데가 없다면
    else:
        # 가장 늦게 사용될 전기 용품의 플러그를 뽑아야 함
        last_use = {item: float('inf') for item in in_use_outlet}
        for j in range(i+1, k):
            if (elec_appliance[j] in in_use_outlet):
                last_use[elec_appliance[j]] = j
            
        appliance_to_remove = max(last_use, key=last_use.get)
        in_use_outlet.remove(appliance_to_remove)
        pulled_out_cnt += 1
        
        in_use_outlet.add(appliance)

print(pulled_out_cnt)