import sys
input = sys.stdin.readline
import heapq
def dij(start):
    dist = [10**9]*(n+1)
    dist[start]=0
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        now_cost, now_idx = heapq.heappop(pq)
        if dist[now_idx]<now_cost:
            continue
        for next_idx,next_cost in graph[now_idx]:
            new_cost = now_cost+next_cost
            if new_cost<dist[next_idx]:
                dist[next_idx] = new_cost
                heapq.heappush(pq,(new_cost,next_idx))
    return dist
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
s,e = map(int,input().split())
dist = dij(s)
print(dist[e])