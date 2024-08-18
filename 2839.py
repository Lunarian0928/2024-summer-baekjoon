n = int(input())

num_of_paperbag = 0
while (n > 0):
    if ((n - 5) % 5 == 0) or ((n - 5) % 3 == 0):
        n -= 5
        num_of_paperbag += 1
    elif ((n - 3) % 5 == 0) or ((n - 3) % 3 == 0):
        n -= 3
        num_of_paperbag += 1
    else:
        break
    
if (n != 0):
    print(-1)
else:
    print(num_of_paperbag)