

def pre_order(T):
    if T:
        print(value[T], end="")
        pre_order(left[T])
        pre_order(right[T])


def in_order(T):
    if T:
        in_order(left[T])
        print(value[T],end="")
        in_order(right[T])


def post_order(T):
    if T:
        post_order(left[T])
        post_order(right[T])
        print(value[T],end="")

num = int(input())
left = [0]*(num+1)
right = [0]*(num+1)
value = ['']*(num+1)
for _ in range(num):
    arr = input().split()
    p = ord(arr[0])-64
    value[p] = arr[0]
    if arr[1] != '.':
        left[p] = ord(arr[1]) - 64
    if arr[2] != '.':
        right[p] = ord(arr[2]) - 64

pre_order(1)
print()
in_order(1)
print()
post_order(1)
