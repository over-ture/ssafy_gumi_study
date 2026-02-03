N = int(input())

A = [0 for _ in range(N)]
B = list(map(int, input().split()))

cnt = 0 # 실행 횟수

while True: # A를 더하는거보다 B를 반대로 0이 될때까지 빼고 나누는 것이 핵심
 
    for num in range(N): # 음수면 -1 
        if B[num] % 2 != 0:
            B[num] -= 1
            cnt += 1 # -1 할때마다 실행횟수 +1
 # 종료조건: 남은 것이 모두 1일때. 그래서 마지막 음수 제거 후 전부 0되면 종료
    if sum(B) == 0: 
        break
    
    is_even = True # 모두 짝수인지 확인
    for x in B:
        if x % 2 != 0:
            is_even = False
            break
    
    if is_even: # 모두 짝수이면 모두 나누기 2
        for num in range(N):
            if B[num] != 0:
                B[num] //= 2
        cnt += 1 # for문 종료 후 실행횟수는 + 1

print(cnt)