def binary_search(target):
    start = 0
    end = n - 1
    
    while True:
        if (start > end):
            break
        
        mid = (start + end) // 2
        
        if (cards[mid] == target):
            return 1
        elif (cards[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
            
    return 0
            
n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
nums = list(map(int, input().split()))

for i in range(m):
    print(binary_search(nums[i]), end = ' ')