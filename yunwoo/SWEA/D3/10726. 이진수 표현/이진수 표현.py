num = int(input())
def switch(n,m):
    for i in range(n):
        if m & (1<<i):
            continue
        else:
            return False
    return True
        
for seq in range(1,num+1):
    n,m = map(int,input().split())
    if switch(n,m):
        print(f"#{seq} ON")
    else:
        print(f"#{seq} OFF")