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

n = int(input())
h = [0] * n
for i in range(n):
    h[i] = int(input())
    
st = stack()
ans = [0] * n
for i in range(1, n + 1):
    ans[i - 1] = 5

# print(ans)
# 왼쪽 위 방향으로 신호를 전달
for i in range(n - 1, -1, -1):
    # 현재 건물의 높이와 비교할 스택에 있는 건물의 높이 비교
    # 스택이 비어있지 않고, 스택의 top에 있는 건물의 높이가 현재 건물의 높이보다 작거나 같다면 pop
    # 현재 건물보다 크거나 같은 건물만을 stack에 남겨두기 위함
    while (not is_empty(st)) and (h[top(st)] < h[i]):
        pop(st)

    if (not is_empty(st)):
        # print("%d번째 건물보다 크거나 같은 건물: %d번째 건물" % (i + 1, top(st) + 1))
        ans[i] = top(st) + 1 - (i + 1) - 1
    else:
        # print("%d번쨰 건물보다 크거나 같은 건물은 없습니다" % (i + 1))         
        ans[i] = n - (i + 1)
    push(st, i)

print(sum(ans))