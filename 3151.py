n = int(input())
a = list(map(int, input().split()))
a.sort()

total_cnt = 0

for i in range(n - 2):
    start = i + 1
    end = n - 1
    
    while start < end:
        current_sum = a[i] + a[start] + a[end]
        
        if current_sum == 0:
            # 만약 start와 end가 같은 값을 가리키는 경우
            if a[start] == a[end]:
                # 그 사이의 값들도 다 같을 것이다.
                # 따라서 조합 개수를 조합 공식에 따라 계산한다
                total_cnt += (end - start) * (end - start + 1) // 2
                break
            # 만약 start와 end가 다른 값을 가리키는 경우
            else:
                left_cnt = 1 
                right_cnt = 1
                # 만약 다음 start가 똑같은 값이라면 개수(left_cnt)를 추가
                while start + 1 < end and a[start] == a[start + 1]:
                    left_cnt += 1
                    start += 1
                
                # 만약 다음 end가 똑같은 값이라면 개수(right_cnt)를 증가
                while end - 1 > start and a[end] == a[end - 1]:
                    right_cnt += 1
                    end -= 1
                                    
                total_cnt += left_cnt * right_cnt

            # 다음 조합을 위해 포인터 이동
            start += 1
            end -= 1
            
        elif current_sum < 0:
            start += 1
        else:
            end -= 1

print(total_cnt)
