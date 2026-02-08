num = int(input())
for seq in range(1,num+1):
    arr = [['!']*15 for _ in range(15)]
    for i in range(5):
        line = input()
        for j in range(15):
            if j < len(line):
                arr[i][j] = line[j]

    print(f'#{seq}',end=" ")
    for x in range(15):
        for y in range(15):
            if arr[y][x]=='!':
                pass
            else:
                print(arr[y][x],end="")
    print()
