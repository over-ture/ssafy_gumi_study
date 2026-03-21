while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for x in range(1, n):
        if n % x == 0:
            arr.append(x)
    if sum(arr) == n:
        print(f"{n} = " + " + ".join(map(str, arr)))
    else:
        print(f"{n} is NOT perfect.")