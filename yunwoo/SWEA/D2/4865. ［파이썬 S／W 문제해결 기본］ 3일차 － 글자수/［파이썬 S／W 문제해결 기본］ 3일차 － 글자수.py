num = int(input())
for seq in range(1,num+1):
    arr = input()
    arr_1 = input()
    dict = {}
    dict_1 = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for i in arr_1:
        if i in dict_1:
            dict_1[i] += 1
        else:
            dict_1[i] = 1
    max_val = 0
    for i in dict_1.keys():
        for j in dict.keys():
            if j in i:
                if max_val <dict_1[i]:
                    max_val = dict_1[i]
    print(f'#{seq} {max_val}')