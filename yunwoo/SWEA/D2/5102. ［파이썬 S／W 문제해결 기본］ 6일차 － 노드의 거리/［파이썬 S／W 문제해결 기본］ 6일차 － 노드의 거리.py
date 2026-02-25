num = int(input())
def bfs(s,g):
    visited = [0]*(v+1)
    q = []
    q.append(s)
    global result
    visited[s] = 1
    while q:
        t = q.pop(0)
        for w in adj[t]:
            if visited[w]==0:
                q.append(w)
                visited[w] = visited[t] + 1
            if w == g:
                result = visited[g]-visited[s]
                break

for seq in range(1,num+1):
    v, e = map(int,input().split())
    adj = [[] for _ in range(v+1)]
    result = 0
    for _ in range(e):
        a, b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
        
    s,g = map(int,input().split())
    bfs(s,g)
    print(f'#{seq} {result}')