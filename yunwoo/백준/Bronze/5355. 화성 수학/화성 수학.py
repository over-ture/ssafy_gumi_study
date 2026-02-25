n = int(input())
for _ in range(n):
    arr =input().split()
    result = float(arr[0])
    for x in arr:
        if x == "@":
            result*=3
        elif x=="%":
            result+=5
        elif x=="#":
            result-=7
    print(f'{result:0.2f}')