import sys

a, b, c = list(map(int, sys.stdin.readline().split()))

# 같은 눈이 3개 = 10000 + (같은눈) x 1000
# 같은 눈이 2개 = 1000 + (같은눈) x 100
# 모두 다른 눈 = (가장 큰 눈) x 100

if a == b == c:
    print(10000 + (a * 1000))
elif (a == b and c != a) or (a == c and c != b):
    print(1000 + (a * 100))
elif b == c and c != a:
    print(1000 + (b * 100))
elif a != b and c != b and c != a:
    print(max(a, b, c) * 100)