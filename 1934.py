t = int(input())

# a, b 중 더 큰 숫자를 구하는 함수
def bigger(a, b):
    if (a > b):
        return a
    else:
        return b
    
# 최대공약수를 구하는 함수
def greatest_common_factor(a, b):
    for i in range(bigger(a, b), 0, -1):
        if (a % i == 0) and (b % i == 0):
            return i

# 최소공배수를 구하는 함수
def least_common_multiple(a, b):
    gcf = greatest_common_factor(a, b)
    return gcf * (a // gcf) * (b // gcf)


arr = []
for i in range(0, t):
    a, b = map(int, input().split())
    lcm = least_common_multiple(a, b)
    arr.append(lcm)

for lcm in arr:
    print(lcm)
    
        