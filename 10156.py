# k: 과자 한 개의 가격
# n: 사려고 하는 과자의 개수
# m: 현재 동수가 가진 돈
k, n, m = map(int, input().split())
# 부족한 돈
shortage = k * n - m
if (shortage < 0): shortage = 0
print(shortage)