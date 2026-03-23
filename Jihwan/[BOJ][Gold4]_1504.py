import math, heapq

def dijkstra(graph, s):
    dist = [math.inf] * (n+1)
    min_heqp = []
    heapq.heappush(min_heqp, [s, 0]) # 출발, 거리
    dist[s] = 0 # 시작 노드는 0
    
    while min_heqp:
        start, distance = heapq.heappop(min_heqp)
        if dist[start] < distance: continue
        for end, weight in graph[start]:
            d = distance + weight
            if d < dist[end]:
                dist[end] = d
                heapq.heappush(min_heqp, [end, d])

    return dist

n, e = map(int, input().split())
way = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    way[a].append((b, w)) # 도착, 거리 튜플 저장
    way[b].append((a, w))

x1, x2 = map(int, input().split())
dist1 = dijkstra(way, x1) # x1 출발 
dist2 = dijkstra(way, x2) # x2 출발
dist_n = dijkstra(way, 1) # 1 출발

case1 = dist_n[x1] + dist1[x2] + dist2[n]
# 1 -> x1 -> x2 -> n
case2 = dist_n[x2] + dist2[x1] + dist1[n]
# 1 -> x2 -> x1 -> n

# x1, x2 를 지나서 n까지의 최단 거리는
# 1 -> x1 -> x2 -> n 와 1 -> x2 -> x1 -> n 중 최소값

if case1 == float('inf') or case2 == float('inf'):
    print(-1)
else:
    print(min(case1, case2))
