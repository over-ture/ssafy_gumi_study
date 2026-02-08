import sys
sys.stdin = open("test.txt")

num = int(input())
for seq in range(1,num+1):
    number = int(input())
    arr = list(map(int, input().split()))
    found = False
    for i in range(1, 1 << number):
        total = 0
        for j in range(number):
            if i & (1 << j):
                total += arr[j]

        if total == 0:
            found = True
            break

    if found:
        print(f'#{seq} 1')
    else:
        print(f'#{seq} 0')
