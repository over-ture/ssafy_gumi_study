import sys ; sys.stdin = open('스위치조작input.txt')


def sol(arr1, arr2):
    global n
    cnt = 0
    for i in range(n):
        if arr1[i] != arr2[i]:
            for j in range(i, n):
                if arr1[j] == 0:
                    arr1[j] = 1
                else:
                    arr1[j] = 0
            cnt += 1
            # arr2와 다른 경우 arr1 스위치
    return cnt

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(f'#{tc} {sol(arr1, arr2)}')