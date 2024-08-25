t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    
    ans = []
    for i in range(2, n + 1):
        while (n % i == 0):
            cnt += 1
            n //= i
        
        if (cnt != 0):
            ans.append((i, cnt))
            cnt = 0
            
        if (n <= 1):
            break
    
    for divisor, cnt in ans:
        print(divisor, cnt)