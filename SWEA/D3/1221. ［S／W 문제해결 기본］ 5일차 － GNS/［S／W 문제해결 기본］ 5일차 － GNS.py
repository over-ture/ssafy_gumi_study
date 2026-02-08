
num = int(input())

for _ in range(num):
    tc, length = input().split()
    length = int(length)

    arr = input().split()

    number = ["ZRO", "ONE", "TWO", "THR", "FOR",
              "FIV", "SIX", "SVN", "EGT", "NIN"]

    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    print(tc) 

    for n in number:
        if n in dic:
            for _ in range(dic[n]):
                print(n, end=" ")
    print()
