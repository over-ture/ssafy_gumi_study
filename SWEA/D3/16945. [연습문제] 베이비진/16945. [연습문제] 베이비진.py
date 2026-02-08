num = int(input())
for j in range(1,num+1):
    number = int(input())
    count = [0]*13
    for _ in range(6):
        count[number %10] += 1
        number //= 10
    i = 0
    cnt = 0
    while i<10:
        if count[i] >= 3:
            count[i] -= 3
            cnt += 1
            continue
        if count[i] >= 1 and count[i+1] >= 1 and count[i+2] >= 1 :
            count[i] -= 1
            count[i+1] -= 1
            count[i+2] -= 1
            cnt += 1
            continue
        i += 1
    if cnt == 2:
        print(f'#{j} 1')
    elif cnt != 2:
        print(f'#{j} 0')