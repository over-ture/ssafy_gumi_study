import sys
input = sys.stdin.readline

N = int(input())

found = False
for x in range(N//5, -1, -1): # x의 범위는 N을 5로 나눈 몫과 같음(그리드 쓸거니까 탐색순서 역순으로)
    for y in range(0, N//3 + 1): # y의 범위는 N을 3으로 나눈 몫과 같음
        if 5*x + 3*y == N: # x 큰수부터 탐색해서 5x + 3y가 있어!
            print(x + y) # 바로 출력 후
            found = True # True 선언
            break
    if found: # 끝까지 못 찾았어
        break
else:
    print(-1)