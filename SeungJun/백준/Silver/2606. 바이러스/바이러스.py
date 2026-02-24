V = int(input())
E = int(input())
visited = [0] * (V+1)
adj = [[] for _ in range(V+1)]
infected = 0
for _ in range(E):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

def dfs(v):
    global infected
    visited[v] = 1
    infected += 1
    for w in adj[v]:
        if visited[w] == 0:
            dfs(w)
dfs(1)
print(infected-1) # 1번 컴퓨터 제외