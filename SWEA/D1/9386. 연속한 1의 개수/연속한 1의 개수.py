num = int(input())
for i in range(1, num+1):
    number = int(input())
    list_1 = list(map(int,input()))
    result = 0
    cnt = 0

    for j in list_1:
        if j == 1:
            cnt += 1
            if result < cnt:
                result = cnt
        else:
            if result < cnt:
                result = cnt
            cnt = 0
    print(f'#{i} {result}')