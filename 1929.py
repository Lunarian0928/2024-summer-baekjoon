import math

m, n = map(int, input().split())
if (m > n):
    upper_bound, lower_bound = m, n
else:
    upper_bound, lower_bound = n, m
    
max_size = 10 ** 6

is_prime = [True for _ in range(max_size + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(max_size)) + 1):
    if (is_prime[i]):
        for j in range(i * i, max_size + 1, i):
                is_prime[j] = False

for i in range(lower_bound, upper_bound + 1):
    if (is_prime[i]):
        print(i)