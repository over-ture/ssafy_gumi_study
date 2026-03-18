import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    N = int(input())
    seq = [] # 값 받아줄 배열
    while len(seq)<N: # arr에 값 넣기
        temp  = list(map(int,input().split()))
        seq.extend(temp)
    print(N//2+1) # 출력할 중앙값 개수 
    i = 0
    result  = [] # 값 하나씩 받아줄 배열 
    cnt = 0
    while i<N: 
        result.append(seq[i]) #값 하나씩 추가
        if i%2==0: #홀수번째 값 출력
            if cnt>=10: #10개씩 출력
                print()
                cnt = 0
            cnt+=1
            result.sort() #정렬
            print(result[len(result)//2],end=" ") #중앙값 출력
        i+=1
    print()