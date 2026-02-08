num = int(input())
for seq in range(1,num+1):
    a,b = map(int,input().split())
    print(f'Case #{seq}: {a} + {b} = {a+b}')