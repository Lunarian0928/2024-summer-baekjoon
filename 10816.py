from collections import Counter

n = int(input()) # 카드의 개수
# 각 카드에 적힌 숫자 정보
cards = list(map(int, input().split()))

# 카드의 숫자 빈도 계산
card_cnt = Counter(cards)

m = int(input())
num = list(map(int, input().split()))

for i in range(m):
    print(card_cnt[num[i]], end = ' ')