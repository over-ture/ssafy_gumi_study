n,m = map(int,input().split())
path = []
used = [0]*(n+1)
def kfc(lev):
    if lev == m:
        print(*path)
        return
    for i in range(1,n+1):
        if used[i]==0:
            path.append(i)
            used[i]=1
            kfc(lev+1)
            path.pop()
            used[i]=0
kfc(0)
