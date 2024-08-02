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

ps = input()
st = stack()

ans = 0

for i in range(len(ps)):
    if ps[i] == '(':
        push(st, ps[i])
    else:
        pop(st)
        if ps[i-1] == '(':
            ans += len(st)
        else:
            ans += 1

print(ans)