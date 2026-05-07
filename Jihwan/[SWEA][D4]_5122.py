T = int(input())
for tc in range(1, T+1):
    # I 인덱스에 수 추가
    # D 인덱스에 수 삭제
    # C 인덱스들 수 교환
    # L 이 없으면 -1 출력
    N, M, L = map(int, input().split()) 
    # N 수열길이 M 추가 횟수, L 출력할 인덱스
    # 5 <= N <= 1000, 1 <= M <= 1000, 6 <= L <= N+M
    # 자연수로 이루어졌다고 하니 0은 없다
    arr = list(map(int, input().split()))
 
    while M > 0:
        M -= 1
        inputs = list(map(str, input().split()))
 
        if inputs[0] == 'I':
            arr.insert(int(inputs[1]), inputs[2])
 
        elif inputs[0] == 'D':
            del arr[int(inputs[1])]
 
        else:
            arr[int(inputs[1])] = inputs[2]
         
 
    if len(arr)-1 >= L:
        print(f'#{tc}', arr[L]) 
    else:
        print(f'#{tc}', -1)