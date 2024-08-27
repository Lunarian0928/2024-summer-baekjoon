def binary_search(target):
    start = 0
    end = n2 - 1
    
    while True:
        if (start > end):
            return True
        
        mid = (start + end) // 2
        
        mid_value = set2[mid]
        if (mid_value == target):
            return False
        elif (mid_value < target):
            start = mid + 1
        else:
            end = mid - 1

n1, n2 = map(int, input().split())

set1 = list(map(int, input().split()))
set1.sort()

set2 = list(map(int, input().split()))
set2.sort()

diff_set = []
for i in range(n1):
    target = set1[i]
    # set1의 요소가 set2에 없는 경우에만 추가
    if (binary_search(target)):
        diff_set.append(target)

print(len(diff_set))
for elem in diff_set:
    print(elem, end = ' ')