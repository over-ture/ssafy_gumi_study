N = int(input())
S = list(input().strip())
stack = []
result = 0
for i in range(N):
    if not stack or stack[-1] == S[i]:
        stack.append(S[i])
    else:
        if stack:
            stack.pop()
    
    result = max(result, len(stack))

if stack:
    print(-1)
else:
    print(result)