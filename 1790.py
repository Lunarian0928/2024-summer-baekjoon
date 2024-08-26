n, k = map(int, input().split())
ans = 0
digit = 1
nine = 9


while k > digit*nine:
    k = k-(digit * nine)
    ans = ans + nine # section의 첫번째 숫자를 구하기 위함
    digit+=1 # 몇 자리인지 구하기 위함 
    nine = nine*10 # 자릿수에 따라 달라지는 section의 길이를 계산하기 위함

# ans + 1: section의 첫번째 숫자를 가리킴
# k-1 // digit
ans = (ans+1) + (k-1) // digit

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])