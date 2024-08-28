n = int(input())
property_values = list(map(int, input().split()))

property_values.sort()  

best_property_sum = float('inf')
best_property_values = []

# 첫 번째 값을 선택하는 루프
for i in range(n - 2):
    left = i + 1
    right = n - 1

    # 두 번째와 세 번째 값을 Two-Pointer로 찾기
    while left < right:
        current_sum = property_values[i] + property_values[left] + property_values[right]

        # 0에 더 가까운 합을 찾으면 업데이트
        if abs(current_sum) < abs(best_property_sum):
            best_property_sum = current_sum
            best_property_values = [property_values[i], property_values[left], property_values[right]]

        # 합이 0보다 크면 right 포인터를 왼쪽으로 이동하여 합을 줄임
        if current_sum > 0:
            right -= 1
        # 합이 0보다 작으면 left 포인터를 오른쪽으로 이동하여 합을 증가시킴
        elif current_sum < 0:
            left += 1
        # 합이 정확히 0이면 최적의 경우이므로 종료
        else:
            break

print(' '.join(map(str, best_property_values)))