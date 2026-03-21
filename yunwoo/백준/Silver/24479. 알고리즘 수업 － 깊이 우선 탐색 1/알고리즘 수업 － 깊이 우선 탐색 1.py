import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x):
    global order
    visited[x] = order
    order += 1
    
    for w in adj[x]:
        if visited[w] == 0:
            dfs(w)

n, m, r = map(int, input().split())

adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)

for i in range(1, n+1):
    adj[i].sort()

order = 1
dfs(r)

print('\n'.join(map(str, visited[1:])))