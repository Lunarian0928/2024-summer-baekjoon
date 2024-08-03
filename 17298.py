def stack():
    return []
    
def is_empty(st):
    return (len(st) == 0)

def top(st):
    if (not is_empty(st)):
        return st[-1]

def push(st, e):
    st.append(e)
    
def pop(st):
    if (not is_empty(st)):
        return st.pop()

# 수열 A의 크기
n = int(input())

seq = list(map(int, input().split()))

st = stack()
nge = [0] * n

for i in range(n - 1, -1, -1):
    # 스택에 현재 값보다 큰 값을 저장하기 위함
    while (not is_empty(st)) and (seq[top(st)] <= seq[i]):
        pop(st)
    if (not is_empty(st)):
        nge[i] = seq[top(st)]
    else:
        nge[i] = -1
    push(st, i)

for ans in nge:
    print(ans, end = ' ')