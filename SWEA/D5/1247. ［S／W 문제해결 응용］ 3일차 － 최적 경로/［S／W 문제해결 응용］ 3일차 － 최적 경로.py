import math
num = int(input())
def kfc(cnt,last_x,last_y,sum_result):
    global min_val, n, visitor, home, visited
    if sum_result>=min_val:
        return
    if cnt ==n: 
        temp = abs(home[0]-last_x)+abs(home[1]-last_y)
        min_val = min(min_val,sum_result+temp)
        return

    for i in range(n):
        if not visited[i]:
            visited[i]=1
            dist = abs(last_x - visitor[i][0]) + abs(last_y - visitor[i][1])
            kfc(cnt+1,visitor[i][0],visitor[i][1],sum_result+dist)
            visited[i] = 0
for seq in range(1,num+1):
    n = int(input())
    arr = list(map(int,input().split()))
    company = [arr[0],arr[1]]
    home = [arr[2],arr[3]]
    visitor=[]
    min_val = 100000000000
    for x in range(4,n*2+3,2):
        visitor.append([arr[x],arr[x+1]])
    visited=[0]*n
    kfc(0,company[0],company[1],0)
    print(f'#{seq} {min_val}')