def dfs(start):
    visited[start] = True
    for w in graph[start]:
        if visited[w] != True:
            dfs(w)
 
for _ in range(10):
    t, E = map(int, input().split()) # t 테스트케이스 번호, E 간선 수
    visited = [False] * (100) # 정점 0 ~ 99
    graph = [[] for _ in range(100)] 
    temp = list(map(int, input().split()))
    S, G = 0, 99
 
    for i in range(E):
        s, e = temp[i*2], temp[i*2+1] 
        graph[s].append(e)
 
    dfs(S)
    if visited[G]:
        print(f'#{t}', 1)
    else:
        print(f'#{t}', 0)