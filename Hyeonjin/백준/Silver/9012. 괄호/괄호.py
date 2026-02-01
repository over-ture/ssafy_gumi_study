import sys
input = sys.stdin.readline

T = int(input())

# + 1, - 1
# '(' ')'

for _ in range(T):
    s = input().strip()

    cnt = 0 # 카운트 초기값 0 설정

    for i in s:
        if i == '(': # '(' 일때 +1
            cnt += 1
        else: # ')' 일때 -1
            cnt -= 1

        if cnt < 0:
            print('NO')
            break


    else:
        if cnt == 0: # 카운트값이 0이면 YES
            print('YES')
        else: # 아니면 NO
            print('NO')