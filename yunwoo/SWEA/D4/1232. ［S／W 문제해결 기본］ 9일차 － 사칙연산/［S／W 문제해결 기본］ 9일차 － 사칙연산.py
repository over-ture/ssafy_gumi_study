def post_order(n):
    if n:
        if left[n] == 0 and right[n] == 0:
            return value[n]
        l = post_order(left[n])
        r = post_order(right[n])
        if value[n] == '+':
            return l + r
        elif value[n] == '-':
            return l - r
        elif value[n] == '*':
            return l * r
        elif value[n] == '/':
            return l / r   
        
for seq in range(1,11):
    n = int(input())
    left = [0]*(n+1)
    right = [0]*(n+1)
    value = ['']*(n+1)
    for _ in range(n):
        arr = list(input().split())
        if len(arr)==2:
            value[int(arr[0])] = int(arr[1])
        elif len(arr)==4:
            value[int(arr[0])] = arr[1]
            left[int(arr[0])]= int(arr[2])
            right[int(arr[0])]= int(arr[3])
    result = int(post_order(1))
    print(f"#{seq} {result}")