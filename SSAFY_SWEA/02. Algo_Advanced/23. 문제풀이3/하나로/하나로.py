import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from heapq import heappush, heappop

# 간선>정점이므로 프림
def prim():
    pq = [(0,0)]
    vis = [0] * n
    ans = 0

    while pq:
        cost, node = heappop(pq)

        if vis[node]:
            continue
        vis[node] = 1
        ans += cost

        for nxt_node in range(n):
            if vis[nxt_node]:
                continue
            nxt_cost = ((x_list[nxt_node] - x_list[node]) ** 2 + (y_list[nxt_node] - y_list[node]) ** 2) * e
            heappush(pq, (nxt_cost, nxt_node))

    return ans



T = int(input())
for tc in range(1,T+1):
    n = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    e = float(input())

    ans = round(prim())

    print(f'#{tc} {ans}')