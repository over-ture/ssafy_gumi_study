dict = {"(": ")", "[": "]", "{": "}", "<": ">"}

for seq in range(1, 11):
    n = int(input())
    arr = list(input())
    stack = []
    result = 0
    for s in arr:
        if s in dict:
            stack.append(s)
        elif s in dict.values():
            if not stack:
                break
            temp = stack.pop()
            if dict[temp] != s:
                break
    else:
        if len(stack) == 0:
            result = 1
    print(f'#{seq} {result}')
