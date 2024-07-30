n = int(input())

dict = {
    "Q1": 0, 
    "Q2": 0, 
    "Q3": 0,
    "Q4": 0,
    "AXIS": 0,
}

for i in range(0, n):
    x, y = map(int, input().split())
    if (x > 0) and (y > 0):
        dict["Q1"] += 1
    elif (x < 0) and (y > 0):
        dict["Q2"] += 1
    elif (x < 0) and (y < 0):
        dict["Q3"] += 1
    elif (x > 0) and (y < 0):
        dict["Q4"] += 1
    else:
        dict["AXIS"] += 1
        
print("Q1: %d" % dict["Q1"])
print("Q2: %d" % dict["Q2"])
print("Q3: %d" % dict["Q3"])
print("Q4: %d" % dict["Q4"])
print("AXIS: %d" % dict["AXIS"]) 