score = int(input())
score /= 10

grade = 'F'
if (score >= 9):
    grade = 'A'
elif (score >= 8):
    grade = 'B'
elif (score >= 7):
    grade = 'C'
elif (score >= 6):
    grade = 'D'
else:
    grade = 'F'
    
print(grade)