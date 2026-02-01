import sys
input = sys.stdin.readline


# 팩토리얼 함수
def factorial(a): 
    fact = 1
    for i in range(1, a + 1):
        fact *= i
    return fact


# 조합 함수
def comb(a, b, c):
    comb = factorial(a + b + c) // (factorial(a) * factorial(b) * factorial(c))
    return comb

###################################################################################

T = int(input())


for _ in range(T):
    n = int(input())

    
    total = 0 # 각각의 조합의 합 초기값 설정

    for x in range(11): # x의 범위는 0부터 10까지
        for y in range(6): # y의 범위는 0부터 5까지
            for z in range(4): # z의 범위는 0부터 3까지

                if x + (2 * y) + (3 * z) == n: # 곱의 합이 10이라면
                    total += comb(x, y, z) # 그 경우의 조합을 구해서 total에 더함

    print(total)