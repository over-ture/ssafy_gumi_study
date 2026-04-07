import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

from heapq import heappush, heappop
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def dijk(start):




T = int(input())
for tc in range(1,T+1):
    inf = 10**18
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

