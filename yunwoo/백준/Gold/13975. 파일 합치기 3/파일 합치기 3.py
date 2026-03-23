import heapq
num =  int(input())
for _ in range(num):
    n = int(input())
    arr = list(map(int,input().split()))
    heap = []
    result = 0
    for x in arr:
        heapq.heappush(heap,x)
    while n>1:
        a=heapq.heappop(heap)
        b=heapq.heappop(heap)
        temp =a+b
        result+=temp
        heapq.heappush(heap,a+b)
        n-=1
    print(result)