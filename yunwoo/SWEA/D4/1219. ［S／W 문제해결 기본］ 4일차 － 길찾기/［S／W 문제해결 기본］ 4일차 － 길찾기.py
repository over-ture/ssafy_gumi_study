def dfs(start, end, N):
    visited = [0] * (N + 1)
    stack = [start]
    while stack:
        v = stack.pop()
        if visited[v]:
            continue
        visited[v] = 1
        if v == end:
            return 1
        for w in graph[v]:
            if visited[w] == 0:
                stack.append(w)
    return 0
for seq in range(1,11):
    v = 99
    graph = [[] for _ in range(v + 1)]
    abcd, e = map(int,input().split())
    arr = list(map(int, input().split()))
    for i in range(e):
        x, y = arr[i*2], arr[i*2+1]
        graph[x].append(y)
    result = dfs(0, 99, v)
    print(f'#{seq} {result}')