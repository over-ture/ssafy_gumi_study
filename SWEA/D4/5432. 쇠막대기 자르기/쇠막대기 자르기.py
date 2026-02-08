num = int(input())
for seq in range(1,num+1):
    arr = input()
    cnt = []
    i = 0
    result = 0
    while i < len(arr):
        if i+1<len(arr) and arr[i] == "(" and arr[i+1] == ")":
            result += len(cnt)
            i += 2
            continue
        if arr[i] == "(":
            cnt.append(i)
        elif arr[i] == ")":
            cnt.pop()
            result +=1
        i+=1
    print(f'#{seq} {result}')


            



            

