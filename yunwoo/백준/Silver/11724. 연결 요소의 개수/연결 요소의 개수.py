import sys
input = sys.stdin.readline
from collections import deque
def bfs(s):
    q = deque([s])
    visited[s]=cnt
    while q:
        x = q.popleft()
        for w in adj[x]:
            if visited[w]==0:
                q.append(w)
                visited[w]=cnt
V,E= map(int,input().split())
adj = [[] for _ in range(V+1)]
for _ in range(E):
    v1,v2 = map(int,input().split())
    adj[v1].append(v2)
    adj[v2].append(v1)
visited=[0]*(V+1)
cnt = 1
bfs(1)
for x in range(1,V+1):
    if visited[x]==0:
        bfs(x)
        cnt+=1
print(cnt)
