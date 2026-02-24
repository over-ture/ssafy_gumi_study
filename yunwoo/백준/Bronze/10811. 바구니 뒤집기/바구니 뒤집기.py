n,m = map(int,input().split())
arr = [0] * (n+1)

for i in range(1,n+1):
    arr[i] = i
for _ in range(m):
    a,b =map(int,input().split())
    arr[b:a-1:-1] = arr[a:b+1]
arr.pop(0)
print(*arr)