def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input())
rings = list(map(int, input().split()))

for i in range(1, n):
    gcd = get_gcd(rings[0], rings[i])
    num = rings[0] // gcd # 분자
    denom = rings[i] // gcd # 분모
    print(f'{num}/{denom}')