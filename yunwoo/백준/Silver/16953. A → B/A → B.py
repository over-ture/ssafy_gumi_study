def check(a,b,cnt):
    global min_val
    if a>b:
        return
    if cnt>min_val:
        return
    if a==b:
        min_val = cnt
        return
    check(a*2,b,cnt+1)
    check(10*a+1,b,cnt+1)
    return -1
a,b = map(int,input().split())
min_val = 10**9
check(a,b,0)
if min_val ==10**9:
    print(-1)
else:
    print(min_val+1)