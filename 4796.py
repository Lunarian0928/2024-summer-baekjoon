days = []
while True:
    # l: 캠핑장을 사용할 수 있는 일 수
    # p: 연속하는 일 수
    # v: 휴가 일 수
    l, p, v = map(int, input().split())
    if (l == 0) and (p == 0) and (v == 0):
        break
    
    days.append(v // p * l + min(v % p, l))

for i in range(len(days)):
    print(f'Case {i+1}: {days[i]}')