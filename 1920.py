n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    ans = 0
    
    start = 0
    end = n - 1
    
    while True:
        if (start > end):
            break
        
        mid = (start + end) // 2
        
        if (arr[mid] == num):
            ans = 1
            break
        elif (arr[mid] < num):
            start = mid + 1
        else:
            end = mid - 1
    
    print(ans)