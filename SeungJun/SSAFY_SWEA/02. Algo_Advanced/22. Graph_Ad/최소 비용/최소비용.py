import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from heapq import heappush, heappop
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def dijk():
    pq = [(0, 0, 0)]
    cost = [[inf] * n for _ in range(n)]
    cost[0][0] = 0

    while pq:
        c, x, y, = heappop(pq)

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                diff = arr[nx][ny] - arr[x][y]
                if diff <= 0:
                    diff = 0

                new_c = c + diff + 1
                if cost[nx][ny] <= new_c:
                    continue
                cost[nx][ny] = new_c
                heappush(pq,(new_c, nx, ny))

    return cost[n-1][n-1]

T = int(input())
for tc in range(1,T+1):
    inf = 10**18
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = dijk()
    print(f'#{tc} {ans}')
