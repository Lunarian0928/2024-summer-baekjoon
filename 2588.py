# a = int(input())
# b = input()

# # 입력받은 문자열을 역순으로 저장하기 위한 변수
# reverse_b = "" 

# # for문을 이용한 문자열 reverse
# for ch in b:
#     reverse_b = ch + reverse_b


# i = 1 # 자릿수
# ans = 0 # 곱셈 결괏값
# for ch in reverse_b:
#     num = int(ch) # 문자를 정수로 변환하여 곱셈에 이용
#     value = a * num # 곱셈 과정을 보여주기 위한 변수
#     print(value)
    
#     value *= i # 자릿수 고려
#     ans += value
#     i *= 10 
    
# print(ans)

a = int(input())
b = input()

length = len(b) + 1
for i in range(1, length):
    print(a * int(b[-i])) # 문자열 슬라이싱 이용

b = int(b)
print(a * b)