<<<<<<< HEAD
T = int(input())
for tc in range(T):
    m = int(input())
    nums = []
    for i in range(m // 10 + 1):
        nums += list(map(int, input().split()))

    print(m // 2 + 1)
    for i in range(1, len(nums) + 1, 2):
        if i > 1 and i % 18 == 1:
            print(sorted(nums[:i])[i // 2])
        else:
            print(sorted(nums[:i])[i // 2], end=' ')
=======
T = int(input())
for tc in range(T):
    m = int(input())
    nums = []
    for i in range(m // 10 + 1):
        nums += list(map(int, input().split()))

    print(m // 2 + 1)
    for i in range(1, len(nums) + 1, 2):
        if i > 1 and i % 18 == 1:
            print(sorted(nums[:i])[i // 2])
        else:
            print(sorted(nums[:i])[i // 2], end=' ')
>>>>>>> f004f55cad382e72c8c19d5d4be06b3603ab15e3
    print() 