def count_cuts(length):
    return sum(cable // length for cable in cables)

def binary_search(target):
    start = 1
    end = max(cables)
    
    while True:
        if (start > end):
            break
            
        mid = (start + end) // 2
        
        if (count_cuts(mid) >= target):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result
            
k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

print(binary_search(n))