import sys
input_line = sys.stdin.readline

def stack():
    return []

def size(st):
    return len(st)

def empty(st):
    return 1 if (size(st) == 0) else 0

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

arr = []
while True:
    st = stack()
    flag = True
    
    s = input_line()

    if (s == '.\n'):
        break
    
    for c in s:
        if (c == '[' or c == '('):
            push(st, c)
        elif (c == ']' or c == ')'):
            if (c == ']' and top(st) == '['):
                pop(st)
            elif (c == ')' and top(st) == '('):
                pop(st)
            else:
                flag = False
                break
    if (not empty(st)):
        flag = False

    arr.append(flag)
    
for ans in arr:
    if (ans):
        print("yes")
    else:
        print("no")