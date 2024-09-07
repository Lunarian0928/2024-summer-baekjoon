n = int(input())
arr = list(map(int, input().split()))

cnt = 0  # 중복이 없는 부분 배열의 수를 세기 위한 변수
subset = set()  # 현재 윈도우 내 중복 없는 요소를 저장할 집합
end = 0 

for start in range(n):
    # end를 가능한 만큼 오른쪽으로 이동하여 중복이 없는 부분 배열을 찾음
    while end < n and arr[end] not in subset:
        subset.add(arr[end])
        end += 1
    
    # 중복이 없는 부분 배열의 수는 현재 윈도우 크기 (end - start)
    cnt += (end - start)
    # print(cnt)
    # start를 오른쪽으로 이동시키면서 현재 요소를 제거
    subset.remove(arr[start])

print(cnt)
