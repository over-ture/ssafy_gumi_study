import heapq
num = int(input())
for seq in range(1,num+1):
    n = int(input())
    pq = []
    arr = list(map(int,input().split()))
    for x in arr:
        heapq.heappush(pq,x)
    total = 0
    idx = n-1
    p = (idx-1)//2
    while p>=0:
        total += pq[p]
        p = (p-1)//2
    print(f'#{seq} {total}')