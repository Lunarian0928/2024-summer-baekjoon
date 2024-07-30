t = int(input())

words = []

for i in range(0, t):
    # r: 반복 횟수, s: 문자열
    r, s = input().split()
    r = int(r)
    
    # word: 각 문자가 r번 반복돼 만들어진 새 문자열
    word = ""
    for ch in s:
        word += ch * r
    words.append(word)
        

for word in words:
    print(word)