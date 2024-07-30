year = int(input())


if (
    # 연도가 4의 배수이면서 100의 배수가 아님
    ((year % 4 == 0) and (year % 100 != 0))
    or 
    # 연도가 400의 배수임
    (year % 400 == 0)
    ):
    print(1)
else:
    print(0)