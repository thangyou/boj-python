import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    a = list(map(int,input().split()))

    if a[0] == 1:
        stack.append(a[1])
    elif a[0] == 2:
        print(stack.pop() if stack else -1)
    elif a[0] == 3:
        print(len(stack))
    elif a[0] == 4:
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)