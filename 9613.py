def get_gcd(num1, num2): # 최대 공약수 계산
    upper_bound = min(num1, num2)
    for divisor in range(upper_bound, 0, -1):
        if (num1 % divisor == 0) and (num2 % divisor == 0):
             return divisor
    return 0

t = int(input())
ans = [0 for _ in range(t)]

for i in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    num_list = data[1:]

    for j in range(0, n):
        for k in range(j+1, n):
            ans[i] += get_gcd(num_list[j], num_list[k])

print("\n".join(map(str, ans)))