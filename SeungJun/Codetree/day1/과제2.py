import sys ; sys.stdin = open('2.txt')

commands = input()

# Please write your code here.
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
nx, ny = 0, 0
dir = 0
cnt = 0
for c in commands:
    cnt += 1
    if c == 'F':
        nx, ny = nx + dxs[dir], ny + dys[dir]
        if nx == ny == 0 :
            print(cnt)
            break
    elif c == 'L':
        dir = (dir+3) % 4
    elif c == 'R':
        dir = (dir+5) % 4
if cnt == len(commands) and (nx != 0 or ny != 0):
    print(-1)