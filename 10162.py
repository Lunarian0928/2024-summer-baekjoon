min = 60 # 1분 = 60초

# 버튼 A, B, C에 지정된 시간
timer = {
    'a': 5 * min, # 5분
    'b': 1 * min, # 1분
    'c': 10 # 10초
}

t = int(input())

# 버튼 A를 누를 수 있는 횟수 
a_cnt = t // timer['a']
t %= timer['a']
# 버튼 B를 누를 수 있는 횟수 
b_cnt = t // timer['b']
t %= timer['b']
# 버튼 C를 누를 수 있는 횟수 
c_cnt = t // timer['c']
t %= timer['c']

if (t == 0):
    print(a_cnt, b_cnt, c_cnt)
else:
    print(-1)