import sys
input = sys.stdin.readline
import heapq
def dij(start):
    dist = [10**9]*(n+1)
    dist[start]=0
    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        now_cost,now_idx = heapq.heappop(pq)
        if dist[now_idx]<now_cost:
            continue
        for next_idx,next_cost in graph[now_idx]:
            new_cost = next_cost+now_cost
            if dist[next_idx]>new_cost:
                dist[next_idx]=new_cost
                heapq.heappush(pq,(new_cost,next_idx))
    return dist
def dij_1(start):
    dist = [[10**9]*2 for _ in range(n+1)]
    dist[start][0]=0
    pq = []
    heapq.heappush(pq,(0,start,0))
    while pq:
        now_cost,now_idx,state = heapq.heappop(pq)
        if dist[now_idx][state] < now_cost:
            continue
        for next_idx,next_cost in graph[now_idx]:
            if state == 0:
                new_cost = next_cost/2+now_cost
            elif state == 1:
                new_cost = next_cost*2+now_cost
            next_state = state^1
            if dist[next_idx][next_state]>new_cost:
                dist[next_idx][next_state]=new_cost
                heapq.heappush(pq,(new_cost,next_idx,next_state))
    return dist
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    c = float(c)
    graph[a].append([b,c])
    graph[b].append([a,c])
dist = dij(1)
dist_1 = dij_1(1)
result = 0
for x in range(1,n+1):
    if dist[x]<min(dist_1[x][0],dist_1[x][1]):
        result+=1
print(result)