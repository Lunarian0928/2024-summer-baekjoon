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


st = stack()
ans = stack()
now = 1
for i in range(n):
    num = int(input())
    while now <= num:
        push(st, now)
        push(ans, '+')
        now += 1
    print(st)        
    if (top(st) == num):
        pop(st)
        push(ans, '-')

print(st)
print(ans)

