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
cnt = 1
for i in range(len(ps)):
    if (ps[i] == '(') or (ps[i] == '['):
        push(st, ps[i])
        if (ps[i] == '('):
            cnt *= 2
        else:
            cnt *= 3 
    else: # ps[i] = ')' or ps[i] = ']'
        if (is_empty(st)): 
            ans = 0
            break
        else:
            top = pop(st)
            if (ps[i] == ')'):
                if (top == '['): # 올바른 VPS가 아닌 경우
                    ans = 0
                    break
                # 괄호가 닫혀 지금까지의 cnt를 더해야 함
                if (ps[i - 1] == '('): 
                    ans += cnt
                else: # ps[i - 1] == ')':
                    pass
                cnt //= 2
            else:
                if (top == '('): # 올바른 VPS가 아닌 경우
                    ans = 0
                    break    
                # 괄호가 닫혀 지금까지의 cnt를 더해야 함
                elif (ps[i - 1] == '['):
                    ans += cnt
                else: # ps[i - 1] == ']':
                    pass
                cnt //= 3 

if (not is_empty(st)):
    ans = 0
    
print(ans)        