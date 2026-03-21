num = int(input())
for seq in range(1,num+1):
    n = int(input())
    time = []
    for x in range(n):
        a,b = map(int,input().split())
        time.append((a,b))
    time.sort(key=lambda x: (x[1], x[0]))
    last_time = 0
    cnt= 0
    for s,e in time:
        if s>=last_time:
            last_time = e
            cnt+=1
    print(f'#{seq} {cnt}')