num = int(input())
def swimming(lev,total_cost):
    global min_val
    if lev>=12:
        min_val = min(min_val,total_cost)
        return
    if min_val<=total_cost:
        return
    swimming(lev+1,total_cost+min(month[lev]*price[0],price[1]))
    swimming(lev + 3, total_cost + price[2])
    
for seq in range(1,num+1):
    price = list(map(int,input().split()))
    month = list(map(int,input().split()))
    min_val = price[3]
    swimming(0,0)
    print(f'#{seq} {min_val}')