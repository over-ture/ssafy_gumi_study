import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
def find(x):
    if x != par[x]:
        par[x] = find(par[x])
    return par[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        par[y] = x

v, e = map(int, input().split())
par = [i for i in range(v+1)]
edge = [] # 가중치들
ans = 0
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c,a,b))

edge.sort(key=lambda x : x[0]) # 가중치 오름차순 정렬

for i in range(e): # 가중치가 작은 순으로 확인
    c, a, b = edge[i]
    if find(a) != find(b): # 두 노드의 대가리가 다르면 최소 스패닝에 추가
        ans += c # 가중치 더하고
        union(a,b) # 추가를 위해 합치기
print(ans)