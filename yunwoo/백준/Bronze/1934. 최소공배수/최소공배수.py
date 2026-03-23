num = int(input())
for _ in range(num):
    n,m = map(int,input().split())
    if n==1 or m==1:
        print(max(n,m))
        continue
    div = 0
    for x in range(2,min(n,m)+1):
        if n%x==0 and m%x==0:
            div = x
    if div==0:
        print(n*m)
    else:
        print(n*m//div)