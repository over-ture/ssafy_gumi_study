import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start] = 0

    while q:
        v = q.popleft()

        if visited[v] == k:
            continue

        for nxt in adj[v]:
            if visited[nxt] == -1:
                visited[nxt] = visited[v] + 1
                q.append(nxt)

n, m, k, x = map(int,input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    adj[a].append(b)

visited = [-1]*(n+1)

bfs(x)

found = False
for i in range(1,n+1):
    if visited[i] == k:
        print(i)
        found = True

if not found:
    print(-1)