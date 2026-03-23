def bfs(x):
    q = [x]
    visited[x]=0
    while q:
        x = q.pop(0)
        for w in adj[x]:
            if visited[w]==-1:
                visited[w]=visited[x]+1
                q.append(w)
n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
min_val = 10**9
result = 0
for x in range(1,n+1):
    visited=[-1]*(n+1)
    bfs(x)
    temp = sum(visited)
    if min_val>temp:
        result = x
        min_val = temp
print(result)
    