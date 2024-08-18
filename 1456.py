import math
max_size = 10 ** 7
is_prime = [True for _ in range(max_size + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, max_size + 1):
    if (is_prime[i] == True):
        for j in range(i + i, max_size + 1, i):
            is_prime[j] = False

cnt = 0
a, b = map(int, input().split())

for i in range(2, max_size + 1):
    if (is_prime[i] == True):
        power = i * i
        while power <= b:
            if (power >= a):
                # print(power)
                cnt += 1 
            if (power > b):
                break
            
            power *= i
print(cnt)