n = int(input())
cnt = 0
result = 0
i=1
while result<n:
    result+=i
    i+=1
    cnt+=1
if result==n:
    print(cnt)
else:
    print(cnt-1)

