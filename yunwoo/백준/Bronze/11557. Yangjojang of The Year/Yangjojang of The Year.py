n = int(input())
for _ in range(n):
    num = int(input())
    max_val=''
    max_idx = 0
    for _ in range(num):
        a,b = map(str,input().split())
        if int(b)>max_idx:
            max_idx = int(b)
            max_val = a
    print(max_val)