n,k = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_val = 0
memo = {}
def kfc(idx, total_w):
    if idx == n:
        return 0
    if (idx, total_w) in memo:
        return memo[(idx, total_w)]
    res = kfc(idx + 1, total_w)
    if total_w + arr[idx][0] <= k:
        res = max(res, kfc(idx + 1, total_w + arr[idx][0]) + arr[idx][1])
    memo[(idx, total_w)] = res
    return res
print(kfc(0,0))