d1, d2, d3 = map(int, input().split())

# 최대를 구하는 함수
def greatest(d1, d2, d3):
    if (d1 > d2) and (d1 > d3):
        return d1
    elif (d2 > d1) and (d2 > d3):
        return d2
    else:
        return d3
    
if (d1 == d2 == d3): # 같은 눈 3개가 나온 경우
    print(10000 + d1 * 1000)
# 모두 다른 눈이 나오는 경우
elif (d1 != d2) and (d1 != d3) and (d2 != d3):
    print(greatest(d1, d2, d3) * 100)
else: # 같은 눈이 2개만 나오는 경우
    if (d1 == d2):
        print(1000 + d1 * 100)
    elif (d1 == d3):
        print(1000 + d1 * 100)
    else:
        print(1000 + d2 * 100)