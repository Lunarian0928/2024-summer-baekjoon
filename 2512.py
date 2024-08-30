n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())

def cal_money(upper_bound):
    return sum(money if (money < upper_bound) else upper_bound for money in arr)


start = 0
end = arr[-1]
best_upper_bound = 0
while (start <= end):
    upper_bound = mid = (start + end) // 2
    
    if (cal_money(upper_bound) == m):
        best_upper_bound = upper_bound
        break
    elif (cal_money(upper_bound) < m):
        start = mid + 1
        if (best_upper_bound < upper_bound):
            best_upper_bound = upper_bound
    else:
        end = mid - 1
        
print(best_upper_bound)