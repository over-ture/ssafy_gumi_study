num = int(input())
for seq in range(1,num+1):
    a,b = map(str, input().split())
    b = list(b)
    result = ''
    for x in b:
        arr = []    
        if x.isdigit():
            x = int(x)
            for _ in range(4):
                arr.append(x%2)
                x//=2
        else:
            a = ord(x)-55
            a= int(a)
            for _ in range(4):
                arr.append(a%2)
                a//=2
        result += "".join(map(str, arr[::-1]))
    print(f'#{seq} {result}')