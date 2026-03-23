import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


def subet_binary1():
    # 1. 0 ~ 부분 집합의 수만큼 반복
    # -i. 부분집합 번호
    result = 10 ** 9
    for i in range(1<<n):
        temp = []
        for idx in range(n):
            if i & (1 << idx): # i와 2^idx를 이진으로 표현했을 때, 둘이 1로 겹치는 자릿수가 있다면
                temp.append(emp[idx])
        total = sum(temp)
        if total >= b and total - b < result:
            result = total - b
    return result


T = int(input())
for tc in range(1,T+1):
    n,b = map(int, input().split())
    emp = list(map(int, input().split()))
    print(f'#{tc} {subet_binary1()}')