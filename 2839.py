# 배달해야 하는 설탕의 무게(kg)
n = int(input())

# 5킬로그램 봉지의 개수
num_of_paperbag5 = n // 5

while True:
    # 3킬로그램 봉지의 개수
    # 5킬로그램 봉지의 개수를 반영하여 저장함
    num_of_paperbag3 = (n - 5 * num_of_paperbag5) // 3
    if (num_of_paperbag5 < 0):
        print(-1)
        break
    
    # 봉지에 담겨있는 설탕 무게와 배달해야 하는 설탕과 같은 경우
    if (5 * num_of_paperbag5 + 3 * num_of_paperbag3 == n):
        print(num_of_paperbag5 + num_of_paperbag3)
        break
    
    # 5킬로그램 설탕의 개수를 감소시킴
    num_of_paperbag5 -= 1