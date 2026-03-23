import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


def quick_sort(left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:  # 교차가 되면 끝
        while i <= j and arr[i] <= pivot:
            i += 1

        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def solve(left, right):
    if left < right:
        piv = quick_sort(left, right)

        solve(left, piv-1)
        solve(piv + 1, right)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    solve(0, len(arr) - 1)
    print(f'#{tc} {arr[n//2]}')