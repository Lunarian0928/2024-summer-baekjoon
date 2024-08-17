max_size = 123456 * 2 
is_prime = [True for _ in range(max_size + 1)]
is_prime[0] = is_prime[1] = False

for i in range(2, max_size + 1):
    if (is_prime[i] == True):
        for j in range(i * i, max_size + 1, i):
            is_prime[j] = False

while True:
    n = int(input())
    if (n == 0):
        break
    print(sum(1 for item in is_prime[n+1:n*2+1] if item))