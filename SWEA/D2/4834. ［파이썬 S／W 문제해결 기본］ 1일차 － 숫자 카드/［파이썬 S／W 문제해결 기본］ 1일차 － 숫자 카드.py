num = int(input())
for i in range(1,num+1):
    number = int(input())
    list_1 = []
    list_1 = list(map(int,input()))
    max_val = list_1[0]
    for j in list_1:
        if max_val < j:
            max_val = j
    counts = [0] * (max_val + 1)
    for x in range(0,number):
        counts[list_1[x]] += 1
    index = counts[0]
    max_number = 0
    count = 0
    for y in counts:
        if y >= index:
            index = y
            max_number = count
            count += 1
        else:
            count += 1
    print(f'#{i} {max_number} {index}')


