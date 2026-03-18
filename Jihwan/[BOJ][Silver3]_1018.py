m, n = map(int, input().split())
arr = [list(map(str, input().strip())) for _ in range(m)]

def cnt_num(lst):
    num = 8 * 8
    check = {'W': 1, 'B': 0}
    for p in range(2):
        color = p
        ex = 0
        for i in range(8):
            for j in range(8):
                if check[lst[i][j]] != color:
                    ex += 1
                color = (color+1)%2
            color = (color+1)%2

        if num > ex:
            num = ex

    return num
        
def chess(r, c):
    board = []
    for k in range(8):
        board.append(arr[r+k][c:c+8])
    return cnt_num(board)

min_num = 8*8
for i in range(m-8+1):
    for j in range(n-8+1):
        ret = chess(i, j)
        if min_num > ret:
            min_num = ret
        
print(min_num)
