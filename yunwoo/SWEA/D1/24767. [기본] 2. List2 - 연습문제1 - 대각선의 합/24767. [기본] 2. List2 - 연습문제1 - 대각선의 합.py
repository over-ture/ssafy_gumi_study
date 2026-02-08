num = int(input())
 
for seq in range(1,num+1):
    number = int(input())
    list_1 = [list(map(int, input().split())) for _ in range(number)]
    result = 0
    for i in range(number):
        for j in range(number):
            if i == j:
                result +=list_1[i][j]
            if number-1-i==j:
                result+=list_1[i][j]
    result -=list_1[2][2]
    print(f'#{seq} {result}')