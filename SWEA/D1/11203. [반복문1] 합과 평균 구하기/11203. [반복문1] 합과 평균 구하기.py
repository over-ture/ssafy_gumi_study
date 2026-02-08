def round_1(a):
    a *= 100
    if a%10 > 5:
        b = a%10
        a-=b
        a+=10
        return a/100
    else:
        b = a % 10
        a -= b
        return a/100


num = int(input())
for seq in range(1, num+1):
    number = int(input())
    arr = list(map(int,input().split()))
    result = round_1(sum(arr)/len(arr))
    print(f'{seq} {sum(arr)} {result}')
