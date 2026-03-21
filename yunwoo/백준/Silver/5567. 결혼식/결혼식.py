def bfs(a):
    cnt = 0
    q = [a]
    visited[a]=0
    while q:
        x = q.pop(0)
        for w in adj[x]:
            if visited[w]==-1:
                visited[w]=visited[x]+1
                if visited[w]<=2:
                    q.append(w)
           
n = int(input())
m = int(input())
adj =[[] for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
visited=[-1]*(n+1)    
bfs(1)
cnt = 0
for i in range(2, n+1):
    if 1 <= visited[i] <= 2:
        cnt += 1
print(cnt)