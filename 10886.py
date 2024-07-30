n = int(input())

cute = 0
not_cute = 0
for i in range(0, n):
    vote = int(input())
    if (vote):
        cute += 1 
    else:
        not_cute += 1
    

if (cute > not_cute):
    print("Junhee is cute!")        
else:
    print("Junhee is not cute!")