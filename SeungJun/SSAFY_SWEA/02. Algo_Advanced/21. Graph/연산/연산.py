import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from collections import deque

def in_range(x):
    return 0 <= x < 1000001

def bfs(v):
    vis[v] = 0
    q = deque([v])
    while q:
        w = q.popleft()
        move = [1, -1, w, -10]
        for d in move:
            nxt = w+d
            if nxt == m and vis[nxt] == -1:
                vis[nxt] = vis[w] + 1
                return #가지치기
            if in_range(nxt) and vis[nxt] == -1:
                vis[nxt] = vis[w]+1
                q.append(nxt)


T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    vis = [-1] * 1000001
    bfs(n)
    print(f'#{tc} {vis[m]}')
