import sys; sys.stdin=open('input.txt')
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1

    for w in adj_lst[v]:
        if not visited[w]:
            dfs(w)

V = int(input())
E = int(input())  # 정점, 간선
#  인접리스트
adj_lst = [[] for _ in range(V + 1)]
#  방문리스트
visited = [0] * (V + 1)

for _ in range(E):
    s, e = map(int, input().split())
    adj_lst[s].append(e)
    adj_lst[e].append(s)


dfs(1)
print(visited.count(1)-1) # 1번 자신 하나 빼고 1 갯수 = 감염된 갯수