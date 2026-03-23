def hit(idx, lst, cnt):
    global ans

    if cnt > ans:
        ans = cnt
    
    if idx == n:
        return
    
    if lst[idx] <= 0:
        hit(idx+1, lst, cnt)
        return
    
    for i in range(n):
        if i == idx or lst[i] <= 0:
            continue

        num = cnt
        k = lst[:]

        k[i] -= eggs[idx][1]
        k[idx] -= eggs[i][1]

        if k[i] <= 0:
            num += 1
        if k[idx] <= 0:
            num += 1

        hit(idx+1, k, num)
    

n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]

s = []
for i in range(n):
    s.append(eggs[i][0])

ans = 0
hit(0, s, 0)

print(ans)