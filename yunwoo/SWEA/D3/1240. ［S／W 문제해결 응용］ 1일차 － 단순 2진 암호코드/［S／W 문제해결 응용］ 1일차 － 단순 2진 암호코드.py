secret = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,'0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
num = int(input())
for seq in range(1,num+1):
    n, m = map(int,input().split())
    maze = [list(input()) for _ in range(n)]
    x,y = 0,0
    found =False
    for a in range(n-1,-1,-1):
        for b in range(m-1,-1,-1):
            if maze[a][b]=='1':
                x,y=a,b
                found = True
                break
        if found:
            break
    arr = maze[x][y-55:y+1]
    i = 0
    odd_result = 0
    even_result = 0 
    value = 0
    for d in range(0,56,7):
        temp = arr[d: d+7]
        temp = ''.join(temp)
        value = secret[temp]
        if i % 2 == 0:
            odd_result += value
        else:
            even_result += value
        i+=1
    if (odd_result*3+even_result)%10==0:
        print(f'#{seq} {odd_result+even_result}')
    else:
        print(f'#{seq} {0}')
