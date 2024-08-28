def binary_search(arr):
    min_property_val = float('inf')
    
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        curr_property_val = arr[start] + arr[end]
        
        if abs(curr_property_val) < abs(min_property_val):
            min_property_val = curr_property_val
        

        if curr_property_val == 0:
            return curr_property_val
        elif curr_property_val < 0:
            start += 1
        else:
            end -= 1
    
    return min_property_val            

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(binary_search(arr))