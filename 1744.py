import math
n = int(input()) # 수열의 크기

positive = []
negative = []
zero = []
for _ in range(n):
    num = int(input())
    if (num > 0):
        positive.append(num)
    elif (num < 0): 
        negative.append(num)
    else:
        zero.append(num)
        
positive.sort(reverse=True)
negative.sort()

ans = 0
while len(positive) > 0:
    if (len(positive) >= 2) and (positive[0] * positive[1] != 1):
        ans += positive[0] * positive[1]
        positive = positive[2::]
    else:
        ans += positive[0]
        positive = positive[1::]

while len(negative) > 0:
    if (len(negative) >= 2):
        ans += negative[0] * negative[1]
        negative = negative[2::]
    else:
        if (len(zero) > 0):
            negative.pop()
            zero.pop()
        else:
            ans += negative[0]
            negative = negative[1::]

print(ans)
            
    
        
    