import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

def explode(board):
    new_board = [["O"] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] == "O":
                new_board[x][y] = "."
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        new_board[nx][ny] = "."
    return new_board

if n == 1:
    result = maze

elif n % 2 == 0:
    result = [["O"] * c for _ in range(r)]

elif n % 4 == 3:
    result = explode(maze)

else:  
    first = explode(maze)
    result = explode(first)

for row in result:
    print("".join(row))