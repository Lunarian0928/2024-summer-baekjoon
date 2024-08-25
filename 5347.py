import sys
input = sys.stdin.read

def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if (a % i == 0) and (b % i == 0):
            return i

def lcm(a, b):
    return a * b // gcd(a, b)

ans = []

data = input().split()
index = 0

n = int(data[index]) # 테스트 케이스의 수
index += 1

for _ in range(n):
    a, b = int(data[index]), int(data[index + 1])
    index += 2
    ans.append(lcm(a, b))

print("\n".join(map(str, ans)))