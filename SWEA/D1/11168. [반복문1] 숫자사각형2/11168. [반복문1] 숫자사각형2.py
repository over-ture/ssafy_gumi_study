import sys
sys.stdin = open("test.txt")

num = int(input())
for seq in range(1,num+1):
    h, w = map(int,input().split())
    arr = [[0]*w for _ in range(h)]
    count = 1
    for i in range(w):
        for j in range(h):
            arr[j][i] = count
            count+=1
    print(f'#{seq}')
    for i in range(h):
        for j in range(w):
            print(arr[i][j],end =" ")
        print()


