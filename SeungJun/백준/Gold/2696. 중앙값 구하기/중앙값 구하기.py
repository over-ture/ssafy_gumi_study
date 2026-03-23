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
    print() 