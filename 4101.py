arr = []
# do while을 Python(파이썬)에서 구현하기
while True:
    a, b = map(int, input().split())
    if (a == 0) and (b == 0):
        break
    else:
        # 삼항 연산자
        arr.append("Yes" if a > b else "No")
        
for i in arr:
    print(i)
