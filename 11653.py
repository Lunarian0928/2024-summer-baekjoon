n = int(input())

i = 2
while ((i <= n) and (n >= 0)):
    if (n % i == 0):
        n //= i
        print(i)
    else:
        i += 1