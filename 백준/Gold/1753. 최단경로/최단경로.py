import sys
input = sys.stdin.readline
import heapq
def dijkstra(start):
    dist = [10**9]*(n+1)
    dist[start] = 0
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        a,b = heapq.heappop(pq)
        if dist[b]<a:
            continue
        for c,d in graph[b]:
            new = a+d
            if new<dist[c]:
                dist[c]=new
                heapq.heappush(pq,(new,c))
    return dist
n,m  =map(int,input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
dist = dijkstra(start)
for x in range(1,n+1):
    if dist[x]==10**9:
        print("INF")
    else:
        print(dist[x])
    
