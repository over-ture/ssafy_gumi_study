import sys
sys.stdin = open("test.txt")

num = int(input())
for seq in range(1, num+1):
    number = int(input())
    arr = [[0]*10 for _ in range(10)]
    for q in range(number):
        x, y, w, h, c = list(map(int,input().split()))
        for i in range(x,w+1):
            for j in range(y,h+1):
                if arr[i][j] ==0 :
                    arr[i][j]=1
                else:
                    arr[i][j]=2
    cnt = 0
    for a in range(10):
        for b in range(10):
            if arr[a][b]==2:
                cnt+=1
    print(f'#{seq} {cnt}')






