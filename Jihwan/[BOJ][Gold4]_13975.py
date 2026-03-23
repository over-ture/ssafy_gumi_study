import heapq

T = int(input())
for _ in range(T):
    n = int(input())
    file = list(map(int, input().split()))

    heapq.heapify(file)
    ans = 0
    while len(file) > 1:
        x = heapq.heappop(file)
        y = heapq.heappop(file)
        
        ans += x + y
        unif = x + y 
        heapq.heappush(file, unif)

    print(ans)