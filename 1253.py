import sys
input = sys.stdin.read

data = input().split()
index = 0

n = int(data[index])
index += 1

a = list(map(int, data[index:index+n]))
a.sort() 

total_cnt = 0

for i in range(n):
    start = 0
    end = n - 1
    
    while (start < end):
        if (start == i):
            start += 1
            continue 
        if (end == i):
            end -= 1
            continue
        
        if (a[start] + a[end] == a[i]):
            total_cnt += 1
            break
        elif (a[start] + a[end] < a[i]):
            start += 1
        else:
            end -= 1

print(total_cnt)