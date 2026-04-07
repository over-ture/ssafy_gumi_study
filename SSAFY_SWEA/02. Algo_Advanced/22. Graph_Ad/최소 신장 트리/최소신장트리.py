import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from heapq import heappush, heappop
def prim(start):
    pq = [(0, start)]
    mst = [0] * (V+1)
    min_w = 0

    while pq:
        w, node = heappop(pq)

        if mst[node]:
            continue
        mst[node] = 1
        min_w += w

        for next_w, next_node in graph[node]:
            if mst[next_node]:
                continue

            heappush(pq, (next_w, next_node))

    return min_w

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())
    graph = [[] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s].append((w, e))
        graph[e].append((w, s))

    print(f'#{tc} {prim(0)}')