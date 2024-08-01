# 더 작은 값을 구하는 함수
def less(n1, n2):
    return n1 if (n1 < n2) else n2

# 문자열에 포함된 각 알파벳의 개수를 저장하는 리스트
cnt1 = [0] * 26
cnt2 = [0] * 26

word1 = input()
word2 = input()

# 반복문을 통해 cnt1, cnt2를 업데이트
for ch in word1:
    cnt1[ord(ch) - ord('a')] += 1
for ch in word2:
    cnt2[ord(ch) - ord('a')] += 1
    
# 애너그램 관계를 위해 제거해야 하는 문자의 개수
removed = 0
for i in range(0, 26):
    if (cnt1[i] != cnt2[i]):
        if (less(cnt1[i], cnt2[i]) == cnt1[i]):
            removed += cnt2[i] - cnt1[i]
        else:
            removed += cnt1[i] - cnt2[i]  
    
print(removed) 