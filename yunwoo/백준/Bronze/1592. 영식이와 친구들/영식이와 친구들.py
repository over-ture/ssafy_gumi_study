n,m,l = map(int,input().split())
arr = [0]*n
x = 0
arr[x]=1
cnt = 0
while True:
    if arr[x]==m:
        break
    if arr[x]%2==1:
        x= (x+l)%n
        arr[x]+=1
        cnt+=1
    elif arr[x]%2==0:
        x = (n-l+x)%n
        arr[x]+=1
        cnt+=1
print(cnt)

