def count_snack(length):
    return sum(snack // length for snack in snacks)

def binary_search(target):
    start = 1
    end = max(snacks)
    
    result = 0
    
    while True:
        if (start > end):
            break
        mid = (start + end) // 2
        
        if (count_snack(mid) >= target):
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return result

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

print(binary_search(m))