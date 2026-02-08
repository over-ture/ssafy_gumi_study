import sys
sys.stdin = open("test.txt")
num = int(input())

for seq in range(1, num + 1):
    h = int(input())
    arr = [[0] * h for _ in range(h)]

    for i in range(h):
        for j in range(h):
            arr[i][j] = (i + 1) * (j + 1)

    print(f'#{seq}')
    for i in range(h):
        for j in range(h):
            print(arr[i][j], end=" ")
        print()
