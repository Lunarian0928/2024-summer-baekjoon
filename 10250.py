import math 

t = int(input())
ans = ['' for _ in range(t)]

for i in range(t):
    # h: 호텔의 층 수
    # w: 각 층의 방수
    # n: 손님의 수
    h, w, n = map(int, input().split())
    
    if (n % h != 0):
        ans[i] += "%d" % (n % h)
    else:
        ans[i] += "%d" % (h)
    
    ans[i] += "%02d" % math.ceil(n / h)
    
print("\n".join(map(str, ans)))