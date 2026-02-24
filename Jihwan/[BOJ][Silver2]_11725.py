def bfs(v): # 위에서부터 내려가면서 방문 표시 하기 때문에
    # 방문표시 안된것들은 자식
    q = [] 
    q.append(v)
    while q:
        t = q.pop(0)
        if not visited[t]: # 방문하지 않았으면
            visited[t] = True # 방문
    
        for w in tree[t]: # 연결된 노드 중에 
            if not visited[w]: # 방문하지 않았다면
                q.append(w) # 큐 삽입
                par[w] = t # 연결된 노드로 들어갔는데 아직 방문 안된것은 자식
                # 부모 표시

n = int(input())
tree = [[] for _ in range(n+1)]
par = [0] * (n+1) # 노드별 부모 노드 기입
visited = [False] * (n+1) # 방문 확인

for _ in range(n-1):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)
    
bfs(1)

for k in range(2, n+1):
    print(par[k])