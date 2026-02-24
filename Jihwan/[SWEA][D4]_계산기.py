T = int(input())

for t in range(1, T+1):
    n = int(input()) # 케이스의 길이
    exp = input() # 중위식 문자열

    #### 후위 표기법 변환 ###
    icp = {'(':3, '*':2, '/':2, '+':1, '-':1} # 스택 밖에서의 우선순위
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1} # 스택 안에서의 우선순위

    stack = []
    ret = '' # 후위식 문자열
    for x in exp:
        if x not in '(+-*/)': # 숫자면 추가
            ret += x
        elif x == ')': # '('까지 pop()
            while stack and stack[-1] != '(':  # peek
                ret += stack.pop()  # 후위식에 추가
            if stack: 
                stack.pop()
        else: # '(+-*/' 사칙 연산자인 경우
            if len(stack) < 1 or isp[stack[-1]] < icp[x]: # 토큰의 우선순위가 더 높으면
                stack.append(x) # push
            elif isp[stack[-1]] >= icp[x]: # 스택 안의 우선순위가 더 높으면
                while stack and isp[stack[-1]] >= icp[x]: # 더 낮은 것이 나올 때까지
                    ret += stack.pop() # 후위식에 추가
                stack.append(x) # push
    while stack:
        ret += stack.pop()
    #### 후위 표기법 변환 ###
    #### 후위 표기법 계산 ###
    stack2 = []
    for y in ret:
        if y not in '(+-*/)': # 숫자면 추가
            stack2.append(int(y))
        else:
            op2 = stack2.pop() # 뒤의 숫자
            op1 = stack2.pop() # 앞의 숫자
            if y == '*': # 우선 순위로 거름
                stack2.append(op1 * op2)
            elif y == '/':
                stack2.append(op1 / op2)
            elif y == '+':
                stack2.append(op1 + op2)
            elif y == '-':
                stack2.append(op1 - op2)

    ans = stack2.pop() # 마지막에 계산 된 수 pop
    print(f'#{t}', ans)