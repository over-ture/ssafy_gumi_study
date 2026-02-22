num = int(input())
for seq in range(1,num+1):
    n = int(input())
    arr = list(map(str,input().split()))
    even = arr[0:int((n+1)/2)]
    odd = arr[int((n+1)/2):n]
    i = 0
    print(f'#{seq}',end = " ")
    while i < len(even):
        print(even[i],end=" ")
        if  i< len(odd):
            print(odd[i],end = " ")
        i+=1
    print()
