num = int(input())
def f(i,n,s):
    global min_v
    if i ==n:
        if min_v>s:
            min_v = s
    elif min_v< s:
        return
    else:
        for j in range(i,n):
            p[i],p[j] = p[j],p[i]
            f(i+1,n,s+arr[i][p[i]])
            p[i],p[j] = p[j],p[i]

for seq in range(1,num+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    min_v = 10000
    f(0,n,0)
    print(f'#{seq} {min_v}')