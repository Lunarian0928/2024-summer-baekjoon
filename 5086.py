arr = []
while True:
    n1, n2 = map(int, input().split())
    if (n1 == 0) and (n2 == 0):
        break
    
    # n1이 n2의 약수일 경우
    if (n1 < n2) and (n2 % n1 == 0):
        arr.append("factor")
    
    # n1이 n2의 배수일 경우
    elif (n1 > n2) and (n1 % n2 == 0):
        arr.append("multiple")
    
    # 둘 다 아닐 경우
    else:
        arr.append("neither")
        
for ans in arr:
    print(ans)