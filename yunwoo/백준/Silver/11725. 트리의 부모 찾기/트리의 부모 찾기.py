n = int(input())
adj = [[] for _ in range(n+1)]
p = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
stack = [1]
p[1]= -1
while stack:
    now = stack.pop()
    for nxt in adj[now]:
        if p[nxt]==0:
            p[nxt]=now
            stack.append(nxt)
for i in range(2, n+1):
    print(p[i])    