
def binary_search(N,key):
    start = 1
    end = N
    count = 0
    while start <= end:
        middle = (start + end) // 2
        count += 1
        if middle == key:
            return count
        elif middle > key:
            end = middle
        else:
            start = middle
    return -1




num = int(input())
for seq in range(1,num+1):
    p, a, b = map(int,input().split())
    result_a = binary_search(p,a)
    result_b = binary_search(p,b)
    print(f'#{seq}', end =" ")
    if result_a < result_b:
        print("A")
    elif result_a > result_b:
        print("B")
    else:
        print(0)

