n, k = map(int, input().split())
num = list(input())

stack = []
dels = k

for i in num:
    while stack and dels > 0 and stack[-1] < i:
        stack.pop()
        dels -= 1
    stack.append(i)

print(''.join(stack[:n-k]))