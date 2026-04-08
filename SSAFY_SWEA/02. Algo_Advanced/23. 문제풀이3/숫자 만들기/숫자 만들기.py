import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def dfs(cnt, total, plus, minus, mul, div):
    global max_v, min_v

    if cnt == n:
        return

    if plus > 0:
        dfs(cnt+1, total+nums[cnt], plus-1, minus, mul, div)
    if minus > 0:
        dfs(cnt+1, total+nums[cnt], plus, minus-1, mul, div)
    if mul > 0:
        dfs(cnt+1, total+nums[cnt], plus, minus, mul-1, div)
    if div > 0:
        dfs(cnt+1, total+nums[cnt], plus, minus, mul, div-1)


T = int(input())
for tc in range(1,T+1):
    n = int(input())

    opers = list(map(int, input().split()))
    nums = list(map(int, input().split()))
