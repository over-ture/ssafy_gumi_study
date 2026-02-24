x = 1
while x < 9:
    x += 1
    n = 0
    while n < 9:
        n += 1
        print(f'{x} * {n} = {x*n}', end=' ')
        if n == 3 or n == 6:
            print('')
    print('\n')