def stack():
    return []

def size(st):
    return len(st)

def empty(st):
    return (len(st) == 0)

def top(st):
    if (empty(st)):
        return -1
    return st[-1]

def push(st, e):
    st.append(e)
    
def pop(st):
    if (empty(st)):
        return -1
    return st.pop()

good_cnt = 0
n = int(input())

for i in range(n):
    flag = True
    
    st = stack()
    word = input()
    
    for c in word:
        if (top(st) == -1):
            push(st, c)
        elif (top(st) == c):
            pop(st)
        else:
            push(st, c)
    
    if (not empty(st)):
        flag = False
    
    if (flag):
        good_cnt += 1
        
print(good_cnt)