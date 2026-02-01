import sys
input = sys.stdin.readline

A, B, N = map(int, input().split())

# * 10^n n => 5   | 10^n 일의 자리에 해당하는 숫자가 소수 n의 자리가 된다. 


num1 = A * (10 ** N) # A에 10의 N제곱만큼 곱한다.

num2 = num1 // B # num1에서 B의 몫나눗셈을 한다. (소숫점 자를거라서)

result = str(num2)[-1] # 마지막에 있는 수가 소수 N번째 자릿수

print(result)