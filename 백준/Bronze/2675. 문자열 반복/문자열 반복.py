n = int(input())
for _ in range(n):
    a,b = map(str,input().split())
    a = int(a)
    for x in b:
        for _ in range(a):
            print(x,end="")
    print()


