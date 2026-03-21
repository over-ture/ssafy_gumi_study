import math
num = int(input())

def score(arr):
    total = 0
    for i in range(len(arr)): 
        for j in range(i+1,len(arr)): 
            total += maze[arr[i]][arr[j]] + maze[arr[j]][arr[i]]
    return total

def select(cnt,start):
    global min_val
    if cnt == n//2:
        temp = score(path)
        path_1 = [x for x in range(n) if x not in path]
        temp_1 = score(path_1)
        min_val = min(min_val, abs(temp-temp_1))
        return

    for x in range(start,n):
        path.append(arr[x])
        select(cnt+1,x+1)
        path.pop()

for seq in range(1,num+1):
    n = int(input())

    maze = [list(map(int,input().split())) for _ in range(n)]
    arr = []
    path = []
    for i in range(n):
        arr.append(i)
    min_val = 10000000
    select(0,0)
    print(f'#{seq} {min_val}')
