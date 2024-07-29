t = int(input())

arr = []
for i in range(0, t):
    op = input().split()
    ans = float(op[0])
    for j in range(1, len(op)):
        if (op[j] == '@'):
           ans *= 3
        elif (op[j] == '%'):
            ans += 5
        elif (op[j] == '#'):
            ans -= 7
    arr.append(ans)
    
for i in arr:
    print("%.2f" % i)