import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = []

for _ in range(n):
    arr = input().split()

    if arr[0] == "push":
        stack.append(arr[1])

    elif arr[0] == "pop":
        if stack:
            result.append(stack.pop())
        else:
            result.append("-1")

    elif arr[0] == "size":
        result.append(str(len(stack)))

    elif arr[0] == "empty":
        if stack:
            result.append("0")
        else:
            result.append("1")

    elif arr[0] == "top":
        if stack:
            result.append(stack[-1])
        else:
            result.append("-1")

print("\n".join(result))