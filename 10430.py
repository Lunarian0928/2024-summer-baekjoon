a, b, c = input().split() # 입력받은 값을 공백을 기준으로 분리

# 문자열을 정수로 변환
a = int(a)
b = int(b)
c = int(c)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)