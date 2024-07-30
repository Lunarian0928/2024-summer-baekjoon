# 포인트 클래스
class Point:
    x = 0 # x좌표 
    y = 0 # y좌표
    # 생성자
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
# 직사각형이 세 점 좌표를 저장하는 리스트
rect = [] 

for i in range(0, 3):
    x, y = map(int, input().split())
    p = Point(x, y)
    rect.append(p)

# 나머지 한 점의 좌표
p = Point()

if (rect[1].x == rect[2].x):
    p.x = rect[0].x
elif (rect[0].x == rect[2].x):
    p.x = rect[1].x
elif (rect[0].x == rect[1].x):
    p.x = rect[2].x
    
if (rect[1].y == rect[2].y):
    p.y = rect[0].y
elif (rect[0].y == rect[2].y):
    p.y = rect[1].y
elif (rect[0].y == rect[1].y):
    p.y = rect[2].y
    
print(p.x, p.y)