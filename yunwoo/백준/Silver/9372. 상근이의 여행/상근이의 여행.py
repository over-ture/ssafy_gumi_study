def bfs(x):
    q = []
    cnt = 1
    q.append(x)
    visited[x]=cnt
    cnt+=1
    while q:
        x = q.pop(0)
        for w in adj[x]:
            if visited[w]==0:
                q.append(w)
                visited[w]=cnt
                cnt+=1

num = int(input())
for _ in range(num):
    n,m = map(int,input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        v1,v2 =map(int,input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
    visited=[0]*(n+1)
    bfs(1)
    print(max(visited)-1)