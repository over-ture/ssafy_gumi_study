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

    print(ans)