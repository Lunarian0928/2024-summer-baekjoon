# 투 포인터 탐색
def two_pointer_search(arr, target):
    start = 0
    end = len(arr) - 1
    
    best_pair = (arr[start], arr[end])
        
    while (start < end):
        # 선택된 두 개 용액을 혼합했을 때의 특성값
        property_val_sum = arr[start] + arr[end]
        
        # property_val_sum이 best_pair의 특성값보다 0에 가까울 경우
        # best_pair를 업데이트 
        if (abs(best_pair[0] + best_pair[1]) > abs(property_val_sum)):
            best_pair = (arr[start], arr[end])
        
        # 특성값이 0이 될 수 있는 경우를 찾았을 경우
        # best_pair를 업데이트하고 바로 리턴
        if (property_val_sum == target):
            best_pair = (arr[start], arr[end])
            break
        # 특성값이 0보다 작은 경우에는
        # 0이 되는 경우를 찾고자 start를 뒤로 이동
        elif (property_val_sum < target):
            start += 1
        # 특성값이 0보다 큰 경우에는
        # 0이 되는 경우를 찾고자 end를 뒤로 이동
        else:
            end -= 1
            
    return best_pair
    
n = int(input()) # 전체 용액의 수
# n개의 용액 특성값 리스트
property_values = list(map(int, input().split()))
# 투 포인터 탐색을 할 수 있도록 정렬
property_values.sort()

# 특성값이 0에 가장 가까운 용액을 만들어 낼 수 있는 경우를 출력
property_val1, property_val2 = two_pointer_search(property_values, 0)
print(property_val1, property_val2)