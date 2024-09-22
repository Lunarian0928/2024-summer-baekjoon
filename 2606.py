computer_cnt = int(input()) # 주어진 컴퓨터의 수
pair_cnt = int(input()) # 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for _ in range(computer_cnt + 1)]
visited = [False] * (computer_cnt + 1) 

for _ in range(pair_cnt):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if (not visited[i]):
            dfs(i)
            
dfs(1)
print(sum(elem for elem in visited[2:]))