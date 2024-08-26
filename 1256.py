from math import comb

def find_kth_string(n, m, k):
    result = [] # k번째 문자열을 저장할 리스트
    
    while n > 0 and m > 0:
        count_a_start = comb(n - 1 + m, n - 1)
        
        if (k <= count_a_start): # k번째 문자열이 현재 'a'로 시작하는 범위 내에 있는 경우
            result.append('a') # a를 결과 문자열에 추가
            n -= 1 # a의 개수를 감소
        else: # k번째 문자열이 현재 'a'로 시작하는 범위를 벗어난 경우
            result.append('z') # z를 추가
            m -= 1 # z의 개수를 감소
            k -= count_a_start # k에서 'a'로 시작하는 모든 경우의 수를 빼서 'z'로 시작하는 경우의 k로 조정

    # 남은 문자들을 모두 result에 추가
    result.extend(['a'] * n)
    result.extend(['z'] * m)
    
    return ''.join(result)

# n: 'a'의 개수, m: 'z'의 개수, k: 문자열 서수
n, m, k = map(int, input().split())

if 0 < k <= comb(n + m, n):
    print(find_kth_string(n, m, k))
else: 
    print(-1)