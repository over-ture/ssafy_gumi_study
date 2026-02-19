import sys ; sys.stdin = open('사냥꾼input.txt')

dxs, dys = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
# 왼쪽부터 반시계방향
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def hunt(x, y):
    global rabbit
    for d in range(8):
        dist = 1
        while True:
            nx, ny = x + dxs[d] * dist, y + dys[d] * dist
            if in_range(nx, ny) and arr[nx][ny] == 2 :
                rabbit += 1 # 토끼
                dist += 1
            elif in_range(nx, ny) and arr[nx][ny] == 3 or in_range(nx, ny) and arr[nx][ny] == 1:
                break # 사냥꾼 or 돌
            elif in_range(nx, ny) and arr[nx][ny] == 0:
                dist += 1 # 빈 공간
            else:
                break

T = int(input())
for tc in range(1, T+1):
    rabbit = 0
    hunters = []
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                hunters.append((i,j))
    for i in hunters:
        hunt(*i)
    print(f'#{tc} {rabbit}')