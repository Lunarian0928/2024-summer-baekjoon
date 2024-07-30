n = int(input())

# 가장 큰 값을 구하는 함수
def greatest(n1, n2, n3):
    if (n1 > n2) and (n1 > n3):
        return n1
    elif (n2 > n1) and (n2 > n3):
        return n2
    else:
        return n3

# 주사위 게임의 상금을 구하는 함수
def get_prize(d1, d2, d3):
    # 같은 눈이 3개가 나올 경우
    if (d1 == d2 == d3):
        return 10000 + d1 * 1000
    # 모두 다른 눈이 나올 경우
    elif (d1 != d2) and (d1 != d3) and (d2 != d3):
        return greatest(d1, d2, d3) * 100
    # 같은 눈이 2개만 나올 경우
    else:
        if (d1 == d2):
            return 1000 + d1 * 100
        elif (d1 == d3):
            return 1000 + d1 * 100
        elif (d2 == d3):
            return 1000 + d2 * 100
        
max = 0 # 가장 많이 받은 상금
for i in range(0, n):
    d1, d2, d3 = map(int, input().split())
    prize = get_prize(d1, d2, d3)
    if (max < prize): 
        max = prize

print(max)