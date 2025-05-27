import sys

def push(stack, x):
    stack.append(x)

def pop(stack):
    if not stack:
        print(-1)
    else:
        print(stack.pop())

def size(stack):
    print(len(stack))

def empty(stack):
    print(1 if not stack else 0)

def top(stack):
    if not stack:
        print(-1)
    else:
        print(stack[-1])

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    input = sys.stdin.readline().split()

    if input[0] == 'push':
        push(stack, input[1])
    elif input[0] == 'pop':
        pop(stack)
    elif input[0] == 'size':
        size(stack)
    elif input[0] == 'empty':
        empty(stack)
    elif input[0] == 'top':
        top(stack)
