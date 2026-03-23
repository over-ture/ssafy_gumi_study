import sys
input = sys.stdin.readline
n,m = map(int,input().split())
def run(level):
    if level==m:
        print(*path)
        return
    for x in range(1,n+1):
        if len(path)>=1 and path[len(path)-1]<=x :
            path.append(x)
            run(level+1)
        elif len(path)==0:
            path.append(x)
            run(level+1)
        else:
            continue
        path.pop()
visited = [0]*(n+1)
arr = []
for i in range(1,n+1):
    arr.append(i)
cnt = 0
path = []
run(0)

