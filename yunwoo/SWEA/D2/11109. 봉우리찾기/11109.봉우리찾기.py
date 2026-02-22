num = int(input())
for seq in range(1, num+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    if n == 1:
        cnt = 1
    else:
        i = 0
        while i < n:
            j = i
            # 같은 높이 끝까지 확장
            while j + 1 < n and arr[j] == arr[j+1]:
                j += 1

            # 봉우리 판정
            if i == 0 and j < n-1:
                if arr[i] > arr[j+1]:
                    cnt += 1
            elif j == n-1 and i > 0:
                if arr[j] > arr[i-1]:
                    cnt += 1
            elif i > 0 and j < n-1:
                if arr[i] > arr[i-1] and arr[j] > arr[j+1]:
                    cnt += 1

            i = j + 1   # 다음 구간으로 이동

    print(f'#{seq} {cnt}')
