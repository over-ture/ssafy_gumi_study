import sys
input = sys.stdin.readline
from collections import deque
def bfs(start):
    queue = deque([start])
    visited[start] = 1
    count = 1
    while queue:
        x = queue.popleft()
        for nxt in adj[x]:
            if not visited[nxt]:
                visited[nxt] = 1
                queue.append(nxt)
                count += 1
    return count
n,m = map(int,input().split())

adj =[[] for _ in range(n+1)]
for _ in range(m):
    v1,v2 = map(int,input().split())
    adj[v2].append(v1)
result = []
max_value = 0
for x in range(1,n+1):
    visited = [0]*(n+1)
    value = bfs(x)
    if value > max_value:
        max_value = value
        result = [x]
    elif value == max_value:
        result.append(x)
print(*result)