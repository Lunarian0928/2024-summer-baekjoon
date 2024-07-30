plates = input()

height = 10
for i in range(1, len(plates)):
    # 그릇을 같은 방향으로 포갰을 경우
    if (plates[i - 1] == plates[i]):
        height += 5
    # 그릇을 반대 방향으로 쌓았을 경우
    else:
        height += 10
    
print(height)