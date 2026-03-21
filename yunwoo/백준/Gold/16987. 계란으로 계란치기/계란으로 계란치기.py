import sys
input = sys.stdin.readline
def check(idx):
    global max_cnt
    if idx ==n:
        cnt = 0
        for x in range(n):
            if s[x]<=0:
                cnt+=1
        max_cnt = max(max_cnt,cnt)
        return
    if s[idx]<=0:
        check(idx+1)
        return
    flag = False
    for x in range(n):
        if idx !=x and s[x]>0:
            flag = True
            s[idx]-=w[x]
            s[x]-=w[idx]
            check(idx+1)
            s[idx]+=w[x]
            s[x]+=w[idx]
    if not flag:
        check(idx+1)

n = int(input())
s = [0]*n 
w = [0]*n 
for x in range(n):
    a,b = map(int,input().split())
    s[x]=a
    w[x]=b
max_cnt = 0
check(0)
print(max_cnt)
