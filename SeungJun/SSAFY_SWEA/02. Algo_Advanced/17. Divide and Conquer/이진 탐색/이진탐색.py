import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def binary_search(arr, num):
    global ans
    l = 0
    r = n - 1
    flag = 0
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == num:
            ans += 1
            return
        elif arr[mid] < num: # 오른쪽에잇음
            l = mid+1
            flag -= 1
        else: # 왼쪽에잇음
            r = mid-1
            flag += 1
        if flag == 2 or flag == -2: #연속 두번 같은방향
            return
    return

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    A.sort()  # 정렬부터
    for i in B:
        binary_search(A, i)
    print(f'#{tc} {ans}')