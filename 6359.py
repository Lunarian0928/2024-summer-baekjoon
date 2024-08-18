t = int(input())
ans = [0 for _ in range(t)]

for i in range(t):
    # n: 감옥의 방 개수
    n = int(input())
    
    # is_locked: 감옥의 각 방이 잠겨있는지 여부
    # 첫 번째 라운드에서 모든 방을 여므로 False
    is_locked = [False for _ in range(n+1)]
    # 단, 0번 방은 사용하지 않기에 True로 설정
    is_locked[0] = True
    
    # k번째 라운드에서 번호가 k의 배수인 방은
    # 열려 있으면 잠그고, 잠겨 있으면 열어야 함
    for j in range(2, n+1):
        for k in range(j, n+1, j):
            is_locked[k] = not is_locked[k]
            
    # 잠겨 있지 않은 방 개수만 세서, ans 요소에 저장
    ans[i] = sum(1 for prisoner in is_locked if not prisoner)
    
print("\n".join(map(str, ans))) # 정답 출력