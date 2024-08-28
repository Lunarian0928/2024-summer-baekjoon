def get_subarr_sums(arr, length):
    subarr_sums = []
    
    for i in range(length):
        sum_val = 0
        for j in range(i, length):
            sum_val += arr[j]
            subarr_sums.append(sum_val)

    subarr_sums.sort() # 추후 이진 탐색을 위해 정렬을 해놓는다
    
    return subarr_sums

def binary_search(target, mod):
    start = 0
    end = len(sub_b_sums) - 1
    
    index = -1 # target value를 발견하지 못한 경우 -1
    while (start <= end):
        mid = (start + end) // 2
        
        # 발견한 경우 인덱스를 업데이트하고
        # 같은 값이 주위에 있는지 확인함
        if (sub_b_sums[mid] == target):    
            index = mid
            
            # 탐색 mod가 first라면 end를 앞으로 이동
            if (mod == 'first'):
                end = mid - 1
            # 탐색 mod가 last라면 start를 뒤로 이동
            elif (mod == 'last'):
                start = mid + 1
            
        elif (sub_b_sums[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
            
    return index        

# t: 테스트 케이스의 수
t = int(input())

n = int(input()) # 배열 a의 크기
a = list(map(int, input().split()))

m = int(input()) # 배열 b의 크기
b = list(map(int, input().split()))

sub_a_sums = get_subarr_sums(a, n) # 부분 배열 a가 가능한 모든 합
sub_b_sums = get_subarr_sums(b, m) # 부분 배열 b가 가능한 모든 합

total_cnt = 0 

# 부분 배열 a가 가능한 합을 탐색하면서
# 부분 배열 b와 더했을 떄 t가 나오는 경우를 탐색함
for sum_a in sub_a_sums:
    target = t - sum_a
    # 이때 똑같은 값이 여러 개 있을 수도 있기 때문에
    # target이 맨 앞에서 발견되는 인덱스와
    # target이 맨 뒤에서 발견되는 인덱스를 이용해
    # 값의 개수를 계산한다
    first_index = binary_search(target, 'first')
    last_index = binary_search(target, 'last')
    
    # 1개라도 발견된 경우
    # T를 만들 수 있는 경우의 수를 합산한다
    if first_index != -1 and last_index != -1:
        cnt = last_index - first_index + 1
        total_cnt += cnt

print(total_cnt)