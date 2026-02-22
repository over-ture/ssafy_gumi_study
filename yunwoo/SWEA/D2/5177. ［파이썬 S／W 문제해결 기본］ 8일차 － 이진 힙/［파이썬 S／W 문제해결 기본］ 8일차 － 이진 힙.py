num = int(input())
def enq(n):
    global last
    last +=1
    heap[last]=n
    c = last
    p = c//2
    while p and heap[p]>heap[c]:
        heap[p], heap[c] = heap[c],heap[p]
        c = p
        p =c//2
for seq in range(1,num+1):
    heap = [0]*501
    last = 0
    n = int(input())
    arr = list(map(int,input().split()))
    for x in arr:
        enq(x)
    result = 0
    while True:
        if last == 0:
            break
        else:
            last//=2
            result+=heap[last]
    print(f'#{seq} {result}')
