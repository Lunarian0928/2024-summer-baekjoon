t = int(input())

arr = []
for i in range(0, t):
    # map 함수를 이용한 여러 개의 변수 입력과 형 변환을 동시 진행
    a, b = map(int, input().split())
    # 배열에 더한 값 추가
    arr.append(a + b)

for i in range(0, t):
    # 형식 지정자를 이용한 정수 출력
    print("Case #%d: %d" % (i + 1, arr[i]))