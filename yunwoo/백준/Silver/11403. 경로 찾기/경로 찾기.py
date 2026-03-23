def bfs(x,y):
    q = [y]
    visited[x][y]=1
    while q:
        y = q.pop()
        visited[x][y]=1
        for w in adj[y]:
            if visited[x][w]==0:
                q.append(w)
                visited[x][w]=1


n = int(input())
maze = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
adj = [[] for _ in range(n)]
for x in range(n):
    for y in range(n):
        if maze[x][y]==1:
            adj[x].append(y)
for x in range(len(adj)):
    for y in adj[x]:
        bfs(x,y)
for x in visited:
    print(*x)