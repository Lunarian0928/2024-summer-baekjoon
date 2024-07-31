import math

def get_factors(n):
    factors = [1]
    for i in range(2, math.ceil(math.sqrt(n))):
        if (n % i == 0):
            factors.append(i)
            factors.append(n // i)
    factors.sort()
    return factors
        
arr = []
while True:
    n = int(input())
    if (n == -1):
        break
    
    factors = get_factors(n)
    sum = 0
    for i in range(0, len(factors)):
        sum += factors[i]
    
    ans = ""
    if (sum == n):
        ans += "%d = " % n
        for i in range(0, len(factors)):
            if (i == len(factors) - 1):
                ans += "%d" % factors[i]
            else:
                ans += "%d + " % factors[i]
        
    else:
        ans = "%d is NOT perfect." % n
    arr.append(ans)
    
for ans in arr:
    print(ans)