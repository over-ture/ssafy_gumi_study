import sys
sys.stdin = open('input.txt', 'r')

c, r = map(int, input().split())
k = int(input())
arr = [[0] * c for _ in range(r)]

start_y, start_x = r-1, 0
arr[start_y][start_x] = 1

drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]
move = 0
cnt = 2

if r*c < k:
    print(0)
else:
    while cnt <= k:
        dr = start_y + drs[move]
        dc = start_x + dcs[move]
        if 0 <= dr < r and 0 <= dc < c and arr[dr][dc] == 0:
            arr[dr][dc] = cnt
            start_y = dr
            start_x = dc
        else:
            move = (move+1)%4
            continue
        cnt += 1            
    
    print(start_x+1, r-start_y)