def count_1(h):
    for i in range(1,h+1):
        print("*"*i+" "*(h-i))
def count_2(h):
    for i in range(h,0,-1):
        print("*" * i+" " * (h - i))
def count_3(h):
    count = 1
    for i in range(1,2*h,2):
        print(" "*(h-count)+"*"*i+" "*(h-count))
        count+=1



num = int(input())
for seq in range(1, num+1):
    height, method = map(int, input().split())
    if method ==1 :
        print(f'#{seq}')
        count_1(height)
    elif method ==2 :
        print(f'#{seq}')
        count_2(height)
    else:
        print(f'#{seq}')
        count_3(height)