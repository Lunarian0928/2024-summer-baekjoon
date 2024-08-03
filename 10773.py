# 스택 생성자
def stack():
    return []

# 스택이 비어있는지 여부를 반환하는 함수
def is_empty(st):
    return (len(st) == 0)

# 스택에 요소를 푸시(push)하는 함수
def push(st, e):
    st.append(e)

# 스택의 탑(top)을 반환하는 함수
def top(st):
    return st[-1]

# 스택의 탑(top)을 제거하고 반환하는 함수
def pop(st):
    return st.pop()

# 입력하는 숫자의 개수
k = int(input())
# 유효한 숫자를 저장하기 위한 스택
st = stack()

for _ in range(k):
    num = int(input())
    
    if (num != 0): # 수를 받아 적음
        push(st, num)
    
    else: # 가장 최근에 쓴 수를 지움
        pop(st)

print(sum(st))