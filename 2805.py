def woods_length(height):
    return sum(tree - height for tree in trees if (tree - height > 0))

def binary_search(target):
    start = 0
    end = max(trees) - 1
    
    result = 0
    
    while True:
        if (start > end):
            break
            
        mid = (start + end) // 2
        
        if (woods_length(mid) >= target):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

n, m = map(int, input().split())
trees = list(map(int, input().split()))
print(binary_search(m))