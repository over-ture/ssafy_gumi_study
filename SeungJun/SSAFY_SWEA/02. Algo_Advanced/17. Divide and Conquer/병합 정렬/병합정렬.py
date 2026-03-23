import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


def merge(left_li, right_li):
    global cnt
    if left_li[-1] > right_li[-1]:
        cnt += 1

    result = [0] * (len(left_li) + len(right_li))
    l = r = 0
    while l < len(left_li) and r < len(right_li):
        if left_li[l] < right_li[r]:
            result[l + r] = left_li[l]
            l += 1
        else:
            result[l + r] = right_li[r]
            r += 1

    # 잔반정리
    while l < len(left_li):
        result[l + r] = left_li[l]
        l += 1

    while r < len(right_li):
        result[l + r] = right_li[r]
        r += 1

    return result


def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)

    merged_list = merge(left_li,right_li)

    return merged_list

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{tc} {result[n//2]} {cnt}')


