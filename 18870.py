def binary_search(target):
    start = 0
    end = length - 1
    
    while True:
        if (start > end):
            break
        
        mid = (start + end) // 2
        mid_elem = sorted_x_set[mid]
        
        if (mid_elem == target):
            return mid
        elif (mid_elem < target):
            start = mid + 1    
        else:
            end = mid - 1
            
    return -1
    
n = int(input())
x = list(map(int, input().split()))

sorted_x_set = sorted(set(x))
print(sorted_x_set)
length = len(sorted_x_set)

for i in range(n):
    target = x[i]
    print(binary_search(target), end = ' ')