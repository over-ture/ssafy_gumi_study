import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def visit(curr, cnt, total):
    global minimum
    if total > minimum:
        return

    if cnt == N-1: # 다 방문했으면 처음 사무실로
        if minimum > total + arr[curr][0]:
            minimum = total + arr[curr][0]
            return

    for nxt in range(1,N):
        if not vis[nxt]:
            vis[nxt] = True
            visit(nxt, cnt + 1, total + arr[curr][nxt])
            vis[nxt] = False # 백트래킹

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minimum = 9999999999
    vis = [False] * N
    visit(0,0,0)
    print(f'#{tc} {minimum}')
