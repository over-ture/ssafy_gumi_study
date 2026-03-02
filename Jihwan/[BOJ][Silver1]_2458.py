from collections import deque

def safe(rn, row, col):
    drs = [0, 0, 1, -1]
    dcs = [1, -1, 0, 0]
    q = deque()
    q.append((row, col))
    visited[row][col] = 1
    
    while q:
        y, x = q.popleft()
        for d in range(4):
            dr = y + drs[d]
            dc = x + dcs[d]
            if 0 <= dr < n and 0 <= dc < n:
                if visited[dr][dc] == 0 and arr[dr][dc] > rn:
                    visited[dr][dc] = 1
                    q.append((dr, dc))

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_v = 0
for i in range(n):
    for j in range(n):
        x = arr[j][i]
        if x > max_v:
            max_v = x
ret = 0
rain = 0

while rain < max_v:

    visited = [[0] * n for _ in range(n)]
    area = 0
    for r in range(n):
        for c in range(n):
            if arr[r][c] > rain and visited[r][c] == 0:
                safe(rain, r, c)
                area += 1
    if ret < area:
        ret = area

    rain += 1

print(ret)