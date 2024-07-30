v = int(input()) # 심사위원의 수
voted = input() # 심사위원이 누구에게 투표했는가

# 각 참가자가 받은 득표수
a = 0
b = 0
for i in range(0, v):
    if voted[i] == 'A':
        a += 1
    else:
        b += 1

# A가 받은 표가 B보다 많은 경우
if (a > b):
    print('A')
# B가 받은 표가 A보다 많은 경우
elif (a < b):
    print('B')
# 비긴 경우
else:
    print("Tie")