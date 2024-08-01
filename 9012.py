# 테스트 케이스의 수
t = int(input())

# 스택이 비어있는지 여부를 return한느 함수
def is_empty(st):
    return (len(st) == 0)

# arr: 결괏값을 저장하는 배열
arr = []

for i in range(0, t):
    # st: VPS인지 확인하기 위한 스택
    st = []
    # is_vps: VPS인지 여부
    is_vps = 1
    
    # ps: 괄호 문자열
    ps = input()
    for ch in ps:
        # 왼쪽 괄호라면 스택에 푸시(push)
        if (ch == '('): 
            st.append(ch)
        # 오른쪽 괄호라면 스택에서 팝(pop)을 시도
        elif (ch == ')'):
            # 스택이 비어있지 않고
            if (not is_empty(st)):
                # 스택의 탑(top)이 왼쪽 괄호가 아니라면
                if (st.pop() != '('):
                    is_vps = 0 # VPS가 아님
                    break
            # 스택이 비어있다면
            else: 
                is_vps = 0 # VPS가 아님
                break
    # 최종적으로 스택이 비어있지 않다면
    if (not is_empty(st)):
        is_vps = 0 # VPS가 아님
    arr.append(is_vps) 
    
for ans in arr:
    if (ans):
        print("YES")
    else:
        print("NO")