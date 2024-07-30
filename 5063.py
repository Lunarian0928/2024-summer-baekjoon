# 테스트 케이스의 개수
n = int(input())
for i in range(0, n):
    # r: 광로르 하지 않았을 때의 수익
    # e: 광고를 했을 때의 수익
    # c: 광고 비용
    r, e, c = map(int, input().split())
    # 광고를 해야 하는 경우
    if (r < (e - c)):
        print("advertise")
    # 광고를 하지 않아야 하는 경우
    elif (r > (e - c)):
        print("do not advertise")
    # 광고를 해도 수익이 차이가 없는 경우
    else:
        print("does not matter")