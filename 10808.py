s = input()
# 리스트 요소의 수는 26으로, 요소는 0으로 초기화
# index 0번 요소는 단어에 포함되어 있는 a의 개수
# index 1번 요소는 단어에 포함되어 있는 b의 개수...
cnts = [0] * 26

for ch in s:
    # ord(): 아스키 코드를 구하는 함수
    cnts[ord(ch) - ord('a')] += 1

for cnt in cnts:
    print("%d" % cnt, end = ' ')