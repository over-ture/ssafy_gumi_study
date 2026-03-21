def bfs(s,e):
    q = [s]
    visited = [0]*(n+1)
    visited[s]=1
    while q:
        x = q.pop(0)
        if x==e:
            print(visited[e]-visited[s])
            break
        for w in adj[x]:
            if not visited[w]:
                visited[w]=visited[x]+1
                q.append(w)

    else:
        print(-1)
n = int(input())
x,y = map(int,input().split())
e = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(e):
    v1,v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
bfs(x,y)