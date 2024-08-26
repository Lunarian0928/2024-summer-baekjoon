from math import *

max_size = 31

t = int(input()) # 테스트 케이스의 수
for _ in range(t):
    x, y = map(int, input().split())
    dist = y - x
    max_k = int(sqrt(dist))
    squared = max_k * max_k
    
    if dist <= 3:
        print(dist)    
    else:
        if (dist == squared):
            print(max_k * 2 - 1)  
        elif (squared <= dist <= squared + max_k):
            print(max_k * 2)
        elif (dist > squared + max_k):
            print(max_k * 2 + 1)