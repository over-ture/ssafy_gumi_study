import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, total):
    global max_val, far_node
    visited[x] = 1
    
    if total > max_val:
        max_val = total
        far_node = x
        
    for next_node, val in adj[x]:
        if visited[next_node] == 0:
            dfs(next_node, total + val)


n = int(input())
adj = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    adj[a].append((b,c))
    adj[b].append((a,c)) 

visited = [0]*(n+1)
max_val = 0
far_node = 1
dfs(1,0)

visited = [0]*(n+1)
max_val = 0
dfs(far_node,0)

print(max_val)