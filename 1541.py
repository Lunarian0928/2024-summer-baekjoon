import re # 정규 표현식 처리

expr = input()
# re.split()으로 여러 구분자를 한 번에 처리
# 캡처 그룹을 통해 분리 기준이 되는 기호도 리스트에 포함
result = re.split(r'(\+|\-)', expr)

# + 연산을 먼저 처리
i = 0
while i < len(result):
    if result[i] == '+':
        # '+' 연산자를 기준으로 양쪽의 숫자를 더함
        sum_value = int(result[i-1]) + int(result[i+1])
        # 리스트에서 처리된 부분을 제거하고 결과를 삽입
        result[i-1:i+2] = [str(sum_value)]
    else:
        i += 1

# - 연산을 처리
i = 0
while i < len(result):
    if result[i] == '-':
        # '-' 연산자를 기준으로 양쪽의 숫자를 뺌
        diff_value = int(result[i-1]) - int(result[i+1])
        # 리스트에서 처리된 부분을 제거하고 결과를 삽입
        result[i-1:i+2] = [str(diff_value)]
    else:
        i += 1

# 최종 결과 출력
print(result[0])