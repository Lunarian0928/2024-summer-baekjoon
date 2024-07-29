t = int(input())

arr = []
for i in range(0, t):
    a, b = map(int, input().split())
    # 첫 번째, 두 번째 요소: 연산자
    # 세 번째 요소: 덧셈 값
    arr.append([a, b, a + b])
    
i = 1
for elem in arr:
    print("Case #%d: %d + %d = %d" %(i, elem[0], elem[1], elem[2]))
    i += 1