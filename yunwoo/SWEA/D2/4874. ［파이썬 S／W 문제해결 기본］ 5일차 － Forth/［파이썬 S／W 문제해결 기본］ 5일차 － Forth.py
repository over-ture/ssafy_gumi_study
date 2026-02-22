num = int(input())
for seq in range(1,num+1):
    stack = [0]*100
    top = -1
    arr = input().split()
    print(f'#{seq} ', end="")
    is_error = False
    for x in arr:
        if x == '.':
            if top == 0:
                print(stack[top])
            else:
                print("error")
            break

        elif x not in '+-/*.':
            top += 1
            stack[top] = int(x)
        else:
            if top < 1:
                print("error")
                is_error = True
                break

            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1

            if x == '+':
                top += 1
                stack[top] = op1 + op2
            elif x == '-':
                top += 1
                stack[top] = op1 - op2
            elif x == '/':
                top += 1
                stack[top] = op1 // op2
            elif x == '*':
                top += 1
                stack[top] = op1 * op2
    if not is_error and '.' not in arr:
        print("error")
