num = int(input())

def kfc(start,height):
    global min_val
    if min_val<height:
        return
    if height>=b:
        min_val = min(min_val, height)
        return
    for x in range(start, n):
        kfc(x+1,arr[x]+height)
for seq  in range(1,num+1):
    n,b =map(int, input().split())
    min_val = 1000000
    arr = list(map(int,input().split()))
    kfc(0,0)
    print(f'#{seq} {min_val-b}')