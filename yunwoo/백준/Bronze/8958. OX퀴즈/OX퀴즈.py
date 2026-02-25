num = int(input())
for _ in range(num):
    arr = input()
    cnt = 1
    result = 0
    for i in arr:
        if i == 'O':
            result+=cnt
            cnt+=1
        else:
            cnt = 1
    print(result)
            