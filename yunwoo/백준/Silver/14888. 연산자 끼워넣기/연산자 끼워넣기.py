import sys
input = sys.stdin.readline

def dfs(idx, value):
    global a,b,c,d,max_val,min_val
    
    if idx == n:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return
    
    if a>0:
        a-=1
        dfs(idx+1, value + arr[idx])
        a+=1
        
    if b>0:
        b-=1
        dfs(idx+1, value - arr[idx])
        b+=1
        
    if c>0:
        c-=1
        dfs(idx+1, value * arr[idx])
        c+=1
        
    if d>0:
        d-=1
        dfs(idx+1, int(value / arr[idx]))
        d+=1


n = int(input())
arr = list(map(int,input().split()))
a,b,c,d = map(int,input().split())

max_val = -10**9
min_val = 10**9

dfs(1, arr[0])

print(max_val)
print(min_val)