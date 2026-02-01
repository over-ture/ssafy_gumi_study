import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))


sort_num = sorted(numbers)


if N % 2 != 0: # N이 홀수라면 
    even_num = []

    for i in range((len(numbers) - 1) // 2): # 범위는 맨 끝값을 뺀 len의 절반
        add = sort_num[i] + sort_num[-2-i] # 맨 끝 값을 제외하고 끝에서부터 하나씩 더해나감
        even_num.append(add)

    if max(even_num) > sort_num[-1]: # 더한 값 중 최댓값이 맨 끝값 보다 크면 
        print(max(even_num)) # 최댓값이 답이고
    else: # 더한 값 중 최댓값이 맨 끝값 보다 작으면
        print(sort_num[-1]) # 맨 끝값이 답이다

else: # N이 짝수라면
    odd_num = []
    
    for i in range(len(numbers) // 2 + 1): # 길이의 절반에서 1 더한 값 만큼
        add = sort_num[i] + sort_num[-1-i] # 양 끝에서부터 하나씩 더해나감
        odd_num.append(add) 
    print(max(odd_num))
