import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
def in_range(x, y):
    return 0 <= x < h and 0 <= y < w
def explode(x, y): # m : 폭발규모(magnitude)
    q = [(x, y)]
    all_bricks = [] # 없어져야 하는 모든 블럭
    vis = [[0] * w for _ in range(h)]
    while q:
        r, c = q.pop(0)
        vis[r][c] = 1
        all_bricks.append((r,c))
        m = arr[r][c] - 1
        for d in range(4):
            nr, nc = r + dr[d] * m, c + dc[d] * m
            if in_range(nr, nc) and not vis[nr][nc]:
                q.append((nr,nc))

    return all_bricks


T = int(input())
for tc in range(1,T+1):
    n, w, h = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(h)]
    for r, c in explode(4,2):
        arr[r][c] = 0
    for i in arr:
        print(i)
    print('##############################')