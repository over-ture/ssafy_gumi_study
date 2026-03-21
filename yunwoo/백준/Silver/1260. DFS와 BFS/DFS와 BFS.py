def dfs(s):
    stack = [s]
    visited = [0]*(V+1)
    while stack:
        x = stack.pop()
        if visited[x]:
            continue
        visited[x] = 1
        print(x, end=" ")
        for w in reversed(adj[x]):  
            if not visited[w]:
                stack.append(w)

def bfs(s):
    q = [s]
    visited=[0]*(V+1)
    visited[s]=1
    while q:
        x = q.pop(0)
        print(x,end=" ")
        for w in adj[x]:
            if visited[w]==0:
                q.append(w)
                visited[w]=1
            
V,E,s = map(int,input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    v1,v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
for i in range(1, V+1):
    adj[i].sort()
dfs(s)
print()
bfs(s)