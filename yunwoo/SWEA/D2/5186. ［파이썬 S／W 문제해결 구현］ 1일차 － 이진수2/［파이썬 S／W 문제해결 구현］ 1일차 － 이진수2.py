num = int(input())
for seq in range(1, num + 1):
    n = float(input())
    arr = ''
    i = -1
    while n > 0:
        if len(arr) >= 13:
            arr = "overflow"
            break
        val = 2**i
        if n >= val:
            arr += '1'
            n -= val  
        else:
            arr += '0'
        i -= 1
    print(f"#{seq} {arr}")