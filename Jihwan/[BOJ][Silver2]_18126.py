from collections import deque

def bfs(v): 
    q = deque()
    q.append(v)
    while q:
        t = q.popleft()
        if visited[t] == -1: # 방문하지 않았으면
            visited[t] = 0 # 방문
    
        for w in tree[t]: # 연결된 노드 중에 
            if visited[w] == -1: # 방문하지 않았다면
                q.append(w) # 큐 삽입
                if t <= w:
                    a, b = t, w
                else:
                    a, b = w, t
                visited[w] = visited[t] + dic[(a, b)]

n = int(input())
visited = [-1] * (n+1)
tree = [[] for _ in range(n+1)]
dic = {}
for i in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    if a <= b: # 작은 방 번호, 큰 방번호 순으로 노드간 거리 저장
        dic[(a, b)] = c
    else:
        dic[(b, a)] = c

bfs(1)

print(max(visited))