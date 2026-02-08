num = int(input())
for seq in range(1, num + 1):
    n, m = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))
    result = [0] * m
    cnt = 0
    for i in list_A:
        if i == list_B[cnt]:
            result[cnt] = i
            cnt += 1
            if cnt == m:
                break
 
    if result == list_B:
        print(f'#{seq} YES')
    else:
        print(f'#{seq} NO')