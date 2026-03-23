arr = input().strip()
bomb = input().strip()
stack = []

i = 0
while i <len(arr):
    stack.append(arr[i])
    if len(stack)>=len(bomb):
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
    i+=1
if stack:
    print(''.join(stack))
else:
    print("FRULA")

