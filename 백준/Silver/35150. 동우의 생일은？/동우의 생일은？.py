from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    a, b, n = map(int, stdin.readline().split())

    if b > a :
        a, b = b, a # 큰거부터 오게 순서 배치
    
    k = n // 2
    if n % 2 == 0:
        print((a*k + b*k) ** 2)
    else:
        print((a*(k+1) + b*k) * (b*(k+1) + a*k))