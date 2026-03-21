n = int(input())
a,b,c=0,0,0
if n//300>=1:
    a+=n//300
    n%=300
if n//60>=1:
    b+=n//60
    n%=60
if n%10==0:
    c+=n//10
    print(a,b,c)
else:
    print(-1)