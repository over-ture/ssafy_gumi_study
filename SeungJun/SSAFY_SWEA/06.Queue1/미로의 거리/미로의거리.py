import sys ; sys.stdin = open('미로의거리input.txt')


def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def bfs(v):
    q = [v]
    visited[v] = 1
    while q:
        v = q.pop(0)
        # 빼내고 이하 할 일

        # --할일--

        # 다음 노드 찾기
        for w in adj[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1 # 거리이므로 누적되어야 함


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n+1)
