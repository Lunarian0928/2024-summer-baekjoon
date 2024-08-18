n = int(input())
count = 0

while n > 0:
    n //= 5 # n을 5로 나누어 5의 배수의 개수를 셈
    count += n # 5의 배수의 개수를 count에 더함

print(count)