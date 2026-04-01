import sys
input = sys.stdin.readline

def test():
    for i in range(n):
        curr = i
        for j in range(h):
            if ladder[j][curr] == 1:
                curr += 1
            elif curr > 0 and ladder[j][curr-1] == 1:
                curr -= 1 
        # 끝까지 가서
        if curr != i:
            return False
    return True

def dfs(step, line, cnt): # line 사다리 step 가로선 cnt 놓는 갯수
    global ans
    if cnt > 3 or cnt >= ans:
        return # pruning
    if test():
        ans = cnt
        return
    if cnt == 3:
        return
    
    for i in range(step, h): 
        start = line if i == step else 0
        for j in range(start, n - 1):
            if ladder[i][j] == 0:
                if j > 0 and ladder[i][j-1] == 1:
                    continue
                if j < n - 2 and ladder[i][j+1] == 1:
                    continue
                
                ladder[i][j] = 1
                dfs(i, j+1, cnt+1)
                ladder[i][j] = 0 # 백트래킹

n, m, h = map(int, input().split())
ladder = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1

ans = float('inf')
dfs(0, 0, 0)

if ans <= 3:
    print(ans)
else:
    print(-1)
