import heapq
import sys

input = sys.stdin.readline

n = int(input())
max_heap = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(max_heap, -x)
    else:
        if len(max_heap) > 0:
            y = heapq.heappop(max_heap)
            print(-y)
        else:
            print(0)