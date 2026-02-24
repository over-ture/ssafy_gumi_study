n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input())

dxs, dys = [1, 0, 1, 0], [0, 1, 0, -1]
# 하-우 상-좌 좌-하 우-상
# 하-우-상-좌 순으로
# 들어오는 방향 dir += 1
dir = (k-1) // n  # 들어오는 방향 설정
if dir == 0:
    x, y = 0, k-1
elif dir == 1:
    x, y = n-1-k, n-1
elif dir == 2:
    x, y = n-1, 3*n-k
else:
    x, y = 4*n-k, 0

nx, ny = x + dxs[dir], y + dys[dir]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

cnt = 0
while in_range(nx, ny):
