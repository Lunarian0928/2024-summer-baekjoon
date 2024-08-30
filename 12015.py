n = int(input())
a = list(map(int, input().split()))

lis = []

def binary_search(arr, x):
    start, end = 0, len(arr) - 1
    while (start <= end):
        mid = (start + end) // 2
        if (arr[mid] < x):
            start = mid + 1
        else:
            end = mid - 1
    return start

for num in a:
    pos = binary_search(lis, num)
    if pos == len(lis):
        lis.append(num)
    else:
        lis[pos] = num
    
# print(lis)
print(len(lis))