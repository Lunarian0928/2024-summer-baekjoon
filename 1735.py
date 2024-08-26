def get_gcd(a, b): # 최대 공약수
    while (b != 0):
        a, b = b, a % b
    return a

def get_lcm(a, b): # 최소 공배수
    return a * b // get_gcd(a, b) 
    
num1, denom1 = map(int, input().split()) 
num2, denom2 = map(int, input().split())

denom = get_lcm(denom1, denom2)
num = num1 * (denom // denom1) + num2 * (denom // denom2)

gcd = get_gcd(num, denom)

num //= gcd
denom //= gcd

print(num, denom)