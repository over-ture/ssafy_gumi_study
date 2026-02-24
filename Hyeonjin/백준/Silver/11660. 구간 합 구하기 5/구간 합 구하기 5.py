import sys
input = sys.stdin.readline

N, M = map(int, input().split())

grid = []

for tc in range(N):
    grid.append(list(map(int,input().split())))

prefix = [([0] * (N+1)) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = grid[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]


for n in range(M):
    x1, y1, x2, y2 = map(int,input().split()) # 2 2 3 4

    a = prefix[x2][y2]
    b = prefix[x2][y1-1]
    c = prefix[x1-1][y2]
    d = prefix[x1-1][y1-1]
    # print(a, b, c, d)

    print(a - b - c + d)