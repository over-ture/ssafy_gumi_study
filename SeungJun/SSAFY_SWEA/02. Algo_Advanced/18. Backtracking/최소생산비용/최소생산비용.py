import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def dfs(row, curr_sum):
    global ans
    if curr_sum > ans: #pruning
        return
    if row == n:
        if curr_sum < ans:
            ans = curr_sum
        return

    for c in range(n):
        if not vis[c]:
            vis[c] = 1
            dfs(row+1, curr_sum + arr[row][c])
            vis[c] = 0


T = int(input())
for tc in range(1,T+1):
     n = int(input())
     arr = [list(map(int, input().split())) for _ in range(n)]
     vis = [0] * n
     ans = 10 ** 9
     dfs(0, 0)
     print(f'#{tc} {ans}')