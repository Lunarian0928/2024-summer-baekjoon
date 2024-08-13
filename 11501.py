t = int(input()) # 테스트 케이스의 수

for _ in range(t):
    n = int(input())
    stock = list(map(int, input().split()))
    
    gain = 0
    high_point = 0
    
    for i in range(n-1, -1, -1):
        if (stock[i] >= high_point):
            high_point = stock[i]    
        if (stock[i] < high_point):
            gain += high_point - stock[i]
            
    print(gain)