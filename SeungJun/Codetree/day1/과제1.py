import sys ; sys.stdin = open('1.txt')

N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
nx, ny = 0, 0
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
mapper = {
    'N' : 0,
    'E' : 1,
    'S' : 2,
    'W' : 3
}
cnt = 0
for i in range(N):
    for j in range(dist[i]):
        cnt += 1
        nx, ny = nx + dxs[mapper[dir[i]]], ny + dys[mapper[dir[i]]]
        if nx == 0 and ny == 0:
            print(cnt)
            break
if cnt == sum(dist) and (nx != 0 or ny != 0) :
    print(-1)