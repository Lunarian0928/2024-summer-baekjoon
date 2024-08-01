# n: 수열의 크기
n = int(input())
# seq: 수열
seq = list(map(int, input().split()))
# x: a_i + a_j와 같은 값
x = int(input())

seq.sort()

cnt = 0


# 투 포인터 방식
left = 0
right = n - 1

while True:
    if (seq[left] + seq[right] == x):
        cnt += 1
        left += 1
        right -= 1
    elif (seq[left] + seq[right] > x):
        right -= 1
    elif (seq[left] + seq[right] < x):
        left += 1
    
    if (left >= right):
        break

print(cnt)