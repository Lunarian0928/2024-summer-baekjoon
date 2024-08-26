n, m = map(int, input().split())

value1 = n
value2 = n - m
value3 = m

def count_factor(n, factor):
    cnt = 0
    while (n > 0):
        n //= factor
        cnt += n
    return cnt

five_cnt1, five_cnt2, five_cnt3 = count_factor(value1, 5), count_factor(value2, 5), count_factor(value3, 5)
two_cnt1, two_cnt2, two_cnt3 = count_factor(value1, 2), count_factor(value2, 2), count_factor(value3, 2)

five_cnt = five_cnt1 - (five_cnt2 + five_cnt3)
two_cnt = two_cnt1 - (two_cnt2 + two_cnt3)

if (five_cnt > 0):
    print(min(five_cnt, two_cnt))
else:
    print(0)