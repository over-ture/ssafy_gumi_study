def is_palindrome(s):
    return s == s[::-1]

for seq in range(1,11):
    length = int(input())
    arr = [list(map(str,input())) for _ in range(8)]
    count = 0
    for i in range(0,8):
        for j in range(0,8-length+1):
            if is_palindrome(arr[i][j:j+length]):
                count += 1

            col = ''
            for k in range(length):
                col += arr[j + k][i]
            if is_palindrome(col):
                count += 1

    print(f'#{seq} {count}')


