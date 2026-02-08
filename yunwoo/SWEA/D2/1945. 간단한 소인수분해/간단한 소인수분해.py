a = int(input())
for seq in range(1,a+1):
    num = int(input())
    a = b = c = d = e = 0
    while num !=1:
        if num %2 == 0:
            num /= 2
            a += 1
        if num %3 == 0:
            num /= 3
            b += 1
        if num %5 == 0:
            num /= 5
            c += 1
        if num %7 == 0:
            num /= 7
            d += 1
        if num %11 == 0:
            num /= 11
            e += 1
    print(f'#{seq} {a} {b} {c} {d} {e}')



