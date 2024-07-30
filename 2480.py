d1, d2, d3 = map(int, input().split())

def greatest(d1, d2, d3):
    if (d1 > d2) and (d1 > d3):
        return d1
    elif (d2 > d1) and (d2 > d3):
        return d2
    else:
        return d3
    
if (d1 == d2 == d3):
    print(10000 + d1 * 1000)
elif (d1 != d2 != d3):
    print(d1 * 100)
else:
    if (d1 == d2):
        print(1000 + d1 * 100)
    elif (d1 == d3):
        print(1000 + d1 * 100)
    else:
        print(1000 + d2 * 100)
    