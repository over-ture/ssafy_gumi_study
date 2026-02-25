import sys
sys.stdin = open("test.txt")
def f(i,k,s,t):
    global cnt
    if s>t:
        return
    if i == k:
        if s == t:
            cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1,k,s+arr[i],t)
        bit[i] = 0
        f(i + 1, k, s, t)
num = int(input())
for seq in range(1,num+1):
    n = int(input())
    result = 0
    arr = list(map(int,input().split()))
    bit = [0]*n
    cnt = 0
    result = f(0,n,0,0)
    if cnt>1:
        print(f'#{seq} 1')
    else:
        print(f'#{seq} 0')