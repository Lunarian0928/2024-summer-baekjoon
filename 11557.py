t = int(input()) # 테스트 케이스의 수

arr = []
for i in range(0, t):
    n = int(input()) # 학교의 수
    dic = {}
    for j in range(0, n):
        # s: 학교 이름
        # l: 소비한 술의 양
        s, l = input().split()
        dic[s] = int(l)
    # sorted를 이용한 value 기준 역순으로 정렬
    sorted_list = sorted(dic.items(), key = lambda item:item[1], reverse=True)
    arr.append(sorted_list[0][0])

for ans in arr:
    print(ans)    