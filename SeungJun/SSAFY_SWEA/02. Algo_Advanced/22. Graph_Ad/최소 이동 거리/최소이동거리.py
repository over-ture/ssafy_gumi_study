import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from heapq import heappush, heappop

def dijk(start):
    pq = [(0, start)]
    dist = [inf] * (N+1)
    dist[start] = 0 # 시작 정점 가중치 0으로

    while pq:
        weight, node = heappop(pq)

        if dist[node] < weight: # 이미 적은 가중치로 왔으면 유기
            continue

        for nxt_weight, nxt_node in graph[node]:
            # 다음 노드로 누적 거리 계산
            new_weight = weight + nxt_weight

            if dist[nxt_node] <= new_weight:
                continue

            # 지금 가려는 누적합이 기존보다 더 작은 값이면
            dist[nxt_node] = new_weight
            heappush(pq, (new_weight, nxt_node))

    return dist

T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)] # 정점 N+1개
    inf = int(10e9)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((w,e)) # 일방통행임

    ans = dijk(0)
    print(f'#{tc} {ans[N]}')