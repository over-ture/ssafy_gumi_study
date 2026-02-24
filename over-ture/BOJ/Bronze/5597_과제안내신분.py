import sys; sys.stdin = open('test.txt')


arr = [int(input()) for _ in range(28)]
chkarr = [0] * 31

for i in arr:
    chkarr[i] = 1

for j in range(1, 31):
    if chkarr[j] == 0:
        print(j)