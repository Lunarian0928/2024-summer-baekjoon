import math

max_size = 1000
is_prime = [True for _ in range(max_size + 1)]
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(max_size)) + 1):
    if is_prime[i]:
        for j in range(i * i , max_size + 1, i):
            is_prime[j] = False

n = int(input())
arr = list(map(int, input().split()))
ans = sum(1 for num in arr if is_prime[num])
print(ans)