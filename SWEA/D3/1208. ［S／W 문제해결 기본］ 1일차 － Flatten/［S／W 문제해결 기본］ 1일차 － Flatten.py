def min_x(list_1):
    min_val = list_1[0]
    index = 0
    count_1 = 0
    for i in list_1:
        if min_val > i:
            min_val = i
            count_1 = index
        index += 1
    return min_val,count_1
def max_x(list_2):
    index = 0
    count = 0
    max_val = list_2[0]
    for i in list_2:
        if max_val < i:
            max_val = i
            count = index
        index += 1
    return max_val,count

for seq in range(1, 11):
    num = int(input())
    list_1 = list(map(int,input().split()))
    for _ in range(num):
        x,idx = max_x(list_1)
        y,idy = min_x(list_1)
        list_1[idx] -= 1
        list_1[idy] += 1
    for i in list_1:
        x_1,_ = max_x(list_1)
        y_1,_ = min_x(list_1)
    print(f'#{seq} {x_1-y_1}')
