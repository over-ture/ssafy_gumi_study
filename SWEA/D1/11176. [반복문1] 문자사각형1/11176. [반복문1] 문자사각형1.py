import sys
sys.stdin = open("test.txt")
num = int(input())

for seq in range(1, num + 1):
    h = int(input())
    arr = [[0] * h for _ in range(h)]
    count = 65
    for i in range(h-1,-1,-1):
        for j in range(h-1,-1,-1):
            if count<=96:
                arr[j][i] =chr(count)
            else:
                count = 65
                arr[j][i] =chr(count) 
            count+=1

    print(f'#{seq}')
    for i in range(h):
        for j in range(h):
            print(arr[i][j], end=" ")
        print()
