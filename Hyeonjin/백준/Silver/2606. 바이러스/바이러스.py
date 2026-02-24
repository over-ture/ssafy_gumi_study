import sys
input = sys.stdin.readline

def dfs(v):  # v 시작 정점

    visited[v] = True  # 방문 표시

    for w in graph[v]:  # 시작 정점의 인접한 정점들: w
        if not visited[w]:  # 방문 안했다면
            dfs(w)

V = int(input())    # 정점
E = int(input())    # 간선

graph = [[] for _ in range(V + 1)]  # 인접리스트 / 0번 안쓰기에 + 1
visited = [0] * (V + 1)             # 방문 리스트

# 인접리스트 요소 받기
computers = []
for _ in range(E):
    computers.append(list(map(int, input().split())))

for line in computers:
    if not line:    # 빈 리스트([])가 들어올 경우를 대비한 예외 처리
        continue

    s, e = line     # 언패킹해서 graph에 집어넣기
    graph[s].append(e)
    graph[e].append(s)  # 양방향일 경우
dfs(1)  # 1번 컴퓨터가 웜 바이러스에 걸렸을 때...

# print(visited)  # [0, True, True, True, 0, True, True, 0]
# print(graph)    # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
print(sum(visited) - 1) # 자기자신 빼기