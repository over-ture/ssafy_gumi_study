num =  int(input())
def exchange(cnt):
    global max_val
    if cnt == m:
        temp = ''.join(n)
        temp = int(temp)
        max_val = max(max_val,temp)
        return
    if (''.join(n),cnt) in subset:
        return
    else:
        subset.add((''.join(n),cnt))
    for i in range(0,len(n)):
        for j in range(i+1,len(n)):
            n[i],n[j] = n[j],n[i]
            exchange(cnt+1)
            n[i],n[j]=n[j],n[i]
for seq in range(1,num+1):
    n,m = input().split()
    n = list(n)
    m = int(m)
    subset = set()
    max_val = 0
    exchange(0)
    print(f'#{seq} {max_val}')
