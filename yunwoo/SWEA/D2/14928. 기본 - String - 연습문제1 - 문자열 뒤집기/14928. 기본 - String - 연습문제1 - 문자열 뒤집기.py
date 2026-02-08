num = int(input())
for seq in range(1, num+1):
    length = int(input())
    arr = list(input())
    print(f'#{seq}',end=" ")
    for i in range(length-1,-1,-1):
        print(arr[i],end="")
    print()