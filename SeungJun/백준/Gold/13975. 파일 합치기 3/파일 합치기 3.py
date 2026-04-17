<<<<<<< HEAD
import heapq

T = int(input())
for tc in range(T):
    n = int(input())
    files = list(map(int, input().split()))
    ans = 0
    heapq.heapify(files) # 리스트를 힙으로 변환 

    while len(files) > 1: # 하나 남을때까지 계속 합치기
        c = heapq.heappop(files)+heapq.heappop(files)
        ans += c
        heapq.heappush(files, c)

=======
import heapq

T = int(input())
for tc in range(T):
    n = int(input())
    files = list(map(int, input().split()))
    ans = 0
    heapq.heapify(files) # 리스트를 힙으로 변환 

    while len(files) > 1: # 하나 남을때까지 계속 합치기
        c = heapq.heappop(files)+heapq.heappop(files)
        ans += c
        heapq.heappush(files, c)

>>>>>>> f004f55cad382e72c8c19d5d4be06b3603ab15e3
    print(ans)