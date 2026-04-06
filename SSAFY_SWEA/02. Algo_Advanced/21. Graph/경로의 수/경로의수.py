import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def dfs(v):
    global cnt
    if v == g:
        cnt += 1
        return
    vis[v] = True
    for w in tree[v]:
        if not vis[w]:
            dfs(w)
            vis[w] = False

T = int(input())
for tc in range(1,T+1):
    n, e = map(int,input().split())
    tree = [[] for _ in range(n+1)]
    inp = list(map(int,input().split()))
    for i in range(len(inp)):
        if i % 2 == 0:
            tree[inp[i]].append(inp[i+1])
    s, g = map(int,input().split())
    vis = [False] * (n+1)
    cnt = 0
    dfs(s)
    print(f'#{tc} {cnt}')
