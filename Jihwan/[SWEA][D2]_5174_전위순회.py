def preorder(n):
    global cnt
    if c1[n]:
        cnt += 1
        preorder(c1[n])
    if c2[n]:
        cnt += 1
        preorder(c2[n])
    else:
        return
 
T = int(input())
for t in range(1, T+1):
    e, n = map(int, input().split()) # e 간선의 개수 / n 서브 트리 루트
    lst = list(map(int, input().split()))
 
    v = e + 1 # 마지막 노드 번호
    c1 = [0] * (v+1)
    c2 = [0] * (v+1)
    par = [0] * (v+1)
 
    for i in range(e):
        p, c = lst[i*2], lst[i*2+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c
 
    cnt = 1
    preorder(n)
    print(f'#{t}', cnt)