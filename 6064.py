import sys
input = sys.stdin.read

data = input().split()

index = 0
t = int(data[index]) # 테스트 데이터의 개수

index = 1
ans = []
for _ in range(t):
    m, n, x, y = int(data[index]), int(data[index + 1]), int(data[index + 2]), int(data[index + 3])
    index += 4 
    
    flag = False
    order = x
    while (order <= m * n):
        if (order - 1) % n + 1 == y:
            flag = True
            break
        order += m
        
    if (flag):
        ans.append(order)
    else:
        ans.append(-1)
        
print("\n".join(map(str, ans)))