arr = list(map(int, input().strip()))
# print(arr)
n = len(arr)

reverse_one_cnt = 1 if (arr[0] == 1) else 0
reverse_zero_cnt = 1 if (arr[0] == 0) else 0

for i in range(1, n):
    # 1을 뒤집는 경우를 판단
    if (arr[i] == 1): 
        # 이전 문자가 0이었다면 i번째의 1부터 뒤집어야 함
        if (arr[i - 1] == 0):
            reverse_one_cnt += 1
        # i-1 ~ i번째의 1을 뒤집으면 되는 것이므로 패스
        else:
            pass

    # 0을 뒤집는 경우를 판단
    else:
        # 이전 문자가 1이었다면 i번째의 0부터 뒤집어야 함
        if (arr[i - 1] == 1):
            reverse_zero_cnt += 1
        # i-1 ~ i번째의 0을 뒤집으면 되는 것이므로 패스
        else:
            pass
        
print(min(reverse_one_cnt, reverse_zero_cnt))