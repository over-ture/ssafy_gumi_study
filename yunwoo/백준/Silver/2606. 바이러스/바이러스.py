num = int(input())
visited = [0] * (num+1)
n = int(input())
adj = [[] for _ in range(num+1)]
for i in range(n):
    v, w = map(int,input().split())
    adj[v].append(w)
    adj[w].append(v)
def DFS(v):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            DFS(w)
DFS(1)
cnt = 0
for i in visited:
    if i==True:
        cnt+=1
print(cnt-1)