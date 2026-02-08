import sys
input = sys.stdin.readline

N = int(input())

paper = [[0]*1001 for _ in range(1001)]

for i in range(0, N):
    x, y, w, h = map(int, input().split())
    for p in range(x, x+w):
        paper[p][y:y+h]= [i+1] * h
            
ans = [0]*(N)

for r in range(1001):
    for c in range(1001):
        if paper[r][c] != 0:
            ans[paper[r][c]-1] += 1


for i in range(0,N):
    print(ans[i])