import sys
input = sys.stdin.read

data = input().split()
# n: 동전의 종류 가짓수, k: 만들어야 하는 가치의 합
n, k = int(data[0]), int(data[1])

coin = list(map(int, data[2:]))
coin.sort(reverse=True)

cnt = 0
for price in coin:
    cnt += k // price  
    k %= price 
    if k == 0:
        break
    
print(cnt)