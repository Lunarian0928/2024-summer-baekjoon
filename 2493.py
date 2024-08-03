def stack():
    return []

def is_empty(st):
    return (len(st) == 0)

def top(st):
    return st[-1]

def push(st, e):
    st.append(e)
    
def pop(st):
    if (not is_empty(st)):
        return st.pop()

n = int(input())  # 탑의 개수 입력
tower = list(map(int, input().split()))  # 각 탑의 높이 입력

ans = [0] * n  # 결과를 저장할 배열 초기화, 초기값은 모두 0
st = stack()  # 스택 초기화

for i in range(n):
    # 현재 탑의 높이와 비교할 스택에 있는 탑의 높이 비교
    # 스택이 비어있지 않고, 스택의 top에 있는 탑의 높이가 현재 탑의 높이보다 작거나 같다면 pop
    while (not is_empty(st)) and (tower[top(st)] <= tower[i]):
        pop(st)
    # 스택이 비어있지 않으면, 현재 탑의 신호를 받을 수 있는 첫 번째 왼쪽 탑의 인덱스를 저장
    if not is_empty(st):
        ans[i] = top(st) + 1  # 1을 더하는 이유는 1-based index로 출력하기 위함
    # 현재 탑의 인덱스를 스택에 추가
    push(st, i)

print(ans)  # 결과 출력
