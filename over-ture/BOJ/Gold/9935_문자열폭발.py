import sys;
input = sys.stdin.readline

txt = input().strip()
bomb = input().strip()

stack = []

for i in txt:
    stack.append(i)
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()
            
res = ''.join(stack)            
print(res if res else 'FRULA')