# 트리의 지름 구하는 법
# 임의의 정점으로부터 가장 먼 정점 a를 찾는다
# a로부터 가장 먼 정점 b를 찾는다
# a-b의 거리가 트리의 지름임
# bfs 시도

from collections import deque

def bfs(v):
    vis = [False] * (n+1)
    vis[v] = True
    distances = [0] * (n+1)
    q = deque([v])

    while q:
        w = q.popleft() # 현재 정점 번호
        for nxt, dist in tree[w]:
            if not vis[nxt]: # 미방문시
                q.append(nxt)
                vis[nxt] = True
                distances[nxt] = distances[w] + dist

    return max(distances), distances.index(max(distances))


n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    p, c, l = map(int, input().split())
    tree[p].append((c,l))
    tree[c].append((p,l))

far_dist, farthest = bfs(1)
print(bfs(farthest)[0])