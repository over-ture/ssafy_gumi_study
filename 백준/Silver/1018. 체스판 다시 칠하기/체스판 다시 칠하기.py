import sys
input = sys.stdin.readline
n,m = map(int,input().split())
chess = [list(input()) for _ in range(n)]
result = n*m
for i in range(n-7):
    for j in range(m-7):
        cnt_b = 0  
        cnt_w = 0  
        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 0:
                    if chess[i+x][j+y] != "B":
                        cnt_b += 1
                    if chess[i+x][j+y] != "W":
                        cnt_w += 1
                else:
                    if chess[i+x][j+y] != "W":
                        cnt_b += 1
                    if chess[i+x][j+y] != "B":
                        cnt_w += 1

        result = min(result, cnt_b, cnt_w)
print(result)