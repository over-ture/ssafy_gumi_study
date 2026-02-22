n = int(input())
arr = list(map(int,input().split()))
ans = []
cnt = 1
for i in arr:
    ans.insert(cnt-i-1,cnt)
    cnt+=1
print(*ans)