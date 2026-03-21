n = int(input())
arr= input()
if arr.count('A')>arr.count('B'):
    print("A")
elif arr.count('A')<arr.count('B'):
    print("B")
else:
    print("Tie")