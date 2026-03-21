path = []
def kfc(x):
    if x==m:
        print(*path)
        return
    for i in range(1,n+1):
        path.append(i)
        kfc(x+1)
        path.pop()
n,m = map(int,input().split())
kfc(0)