n = int(input())
arr = []
end_time = 0
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort(key = lambda x : (x[1],x[0]))
cnt = 0
for s,e in arr:
    if s>=end_time:
        cnt+=1
        end_time = e
print(cnt)