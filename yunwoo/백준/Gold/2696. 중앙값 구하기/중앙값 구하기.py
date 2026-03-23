tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = []
    while len(arr)<n:
        temp  = list(map(int,input().split()))
        arr.extend(temp)
    print(n//2+1)
    i = 0
    result  = []
    cnt = 0
    while i<n:
        result.append(arr[i])

        if i%2==0:
            if cnt>=10:
                print()
                cnt = 0
            cnt+=1
            result.sort()
            print(result[len(result)//2],end=" ")
        i+=1
    print()