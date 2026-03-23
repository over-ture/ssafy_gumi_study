def bfs(x):
   q = [x]
   visited[x]=1
   while q:
        x = q.pop(0) 
        visited[x]=1
        for w in adj[x]:
            if visited[w]==0:
                q.append(w)
                visited[w]=1
num = int(input())
for _ in range(num):
    n = int(input())
    arr = list(map(int,input().split()))
    adj = [[] for _ in range(n+1)]
    for x in range(1,n+1):
        adj[x].append(arr[x-1])
    visited= [0]*(n+1)
    cnt = 0
    for x in range(1,n+1):
        if visited[x]==0:
            bfs(x)
            cnt+=1
    print(cnt)