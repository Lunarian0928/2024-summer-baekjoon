t = int(input())

max_size = 10000

is_prime = [True for _ in range(max_size + 1)]
is_prime[0] = is_prime[1] = True

for i in range(2, max_size + 1):
    if (is_prime[i]):
        for j in range(i + i, max_size + 1, i):
            is_prime[j] = False

for _ in range(t):
    n = int(input())
    for n1 in range(n // 2, 1, -1):
        n2 = n - n1
        if (is_prime[n1] == True) and (is_prime[n2] == True):
            print(n1, n2)
            break