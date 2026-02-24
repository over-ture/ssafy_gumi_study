num = int(input())

def dfs(start,end,N):
    visited = [0] *(N+1)
    stack = [start]
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = 1
        if v == end:
            return 1
        for w in graph[v]:
            if visited[w]==0:
                stack.append(w)
    return 0

for seq in range(1,num+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for i in range(e):
        a, b = map(int,input().split())
        graph[a].append(b)
    start, end = map(int,input().split())
    result = dfs(start,end,v)
    print(f'#{seq} {result}')