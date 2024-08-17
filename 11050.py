max_size = 10
fact = [0 for _ in range(max_size + 1)]
fact[0] = fact[1] = 1

for i in range(2, max_size + 1):
    fact[i] = i * fact[i - 1]

n, k = map(int, input().split())
binomial_coefficient = fact[n] // (fact[n-k] * fact[k])
print(binomial_coefficient)